%define version_major 5.15
%define version_patch 2

Name:       libqt
Version:    %{version_major}.%{version_patch}
Release:    2%{?dist}
Summary:    Cross-platform application and UI framework

License:    GFDLv1.3, GPLv2, GPLv3, LGPLv2, LGPLv3
URL:        https://www.qt.io
%undefine   _disable_source_fetch
Source0:    https://download.qt.io/official_releases/qt/%{version_major}/%{version}/single/qt-everywhere-src-%{version}.tar.xz
%define     SHA256SUM0 3a530d1b243b5dec00bc54937455471aaa3e56849d2593edb8ded07228202240

# Patch here from Homebrew
Patch0:     https://raw.githubusercontent.com/Homebrew/formula-patches/92d4cf/qt/5.15.2.diff#/libqt-0001-find-11.0-sdk.patch

Patch1:     libqt-0002-export-all-staticmetaobjects.patch

BuildRequires:  pkg-config
BuildRequires:  libsqlite-devel
BuildRequires:  libfreetype-devel
#BuildRequires:  libpcre2-devel

Requires:       libsqlite
Requires:       libfreetype-devel
#Requires:       libpcre2-devel

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developin

%package     -n qt
Summary:        Command-line programs and utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n qt

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n qt-everywhere-src-%{version} -p1

%ifarch aarch64
sed -e 's/stat64/stat/' -i.orig qt3d/src/3rdparty/assimp/contrib/zip/src/miniz.h
%endif

%build

./configure \
    -verbose \
    -prefix %{_prefix} \
    -archdatadir %{_datadir} \
    -datadir %{_datadir} \
    -release \
    -opensource -confirm-license \
    -system-zlib \
    -qt-libpng \
    -qt-libjpeg \
    -system-freetype \
    -qt-pcre \
    -nomake examples -nomake tests \
    -no-rpath \
    -pkg-config \
    -dbus-runtime \
    QMAKE_APPLE_DEVICE_ARCHS=%(uname -m)

%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# QtUiTools.framework is required for shiboken / pyside2 to build correctly, but
# building it _not_ as a framework is required for Qt itself to work. TODO.
# Qt officially blames this on Homebrew passing stupid -Isystem flags. We don't do
# that. Real funny how I still have to build uitools twice then.

# Patch 0002 is also involved in this process, as QtUiTools has broken symbol visibility
# in the normal build.

patch -p1 <<EOF
--- a/qttools/src/designer/src/uitools/uitools.pro	2020-12-19 21:53:15.000000000 -0800
+++ b/qttools/src/designer/src/uitools/uitools.pro	2020-12-19 21:53:25.000000000 -0800
@@ -1,5 +1,4 @@
 TARGET = QtUiTools
-CONFIG += static

 include(../lib/uilib/uilib.pri)

@@ -9,8 +8,7 @@
 SOURCES += quiloader.cpp

 DEFINES += \\
-    QFORMINTERNAL_NAMESPACE \\
-    QT_DESIGNER_STATIC
+    QFORMINTERNAL_NAMESPACE

 # QtUiPlugins end up in designer for historical reasons. However, if
 # designer isn't actually built, we need to claim the plugin type here.

EOF
cd qttools/src/designer/src/uitools
make -B
make install INSTALL_ROOT=%{buildroot}

pushd %{buildroot}%{_libdir}
for prl_file in libQt5*.prl ; do
  sed -i "" -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  rm -fv "$(basename ${prl_file} .prl).la"
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    sed -i "" -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

# can I get an uhhhhhhhh mangle-shebangs.sh
find %{buildroot} -type f | xargs sed -i "" -e '1s:/usr/bin/python:/usr/local/bin/python3:'

%files
%{_libdir}/*.framework
%{_datadir}/qml
%{_datadir}/plugins
%{_datadir}/translations
%{_datadir}/phrasebooks
%doc %{_datadir}/doc

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.prl
%{_libdir}/pkgconfig/*.pc
%{_libdir}/metatypes
%{_libdir}/cmake/*
%{_datadir}/mkspecs

%files -n qt
%{_bindir}/*

%changelog
