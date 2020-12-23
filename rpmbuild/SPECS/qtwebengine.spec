# not yet complete, needs Xcode

Name:           qtwebengine
Version:        5.15.2
Release:        1%{?dist}
Summary:        QTWebEngine from libqt

License:    GFDLv1.3, GPLv2, GPLv3, LGPLv2, LGPLv3
URL:        https://www.qt.io
%undefine   _disable_source_fetch
Source0:    https://download.qt.io/official_releases/qt/%{version_major}/%{version}/single/qt-everywhere-src-%{version}.tar.xz
%define     SHA256SUM0 3a530d1b243b5dec00bc54937455471aaa3e56849d2593edb8ded07228202240

# Patch here from Homebrew
Patch0:     https://raw.githubusercontent.com/Homebrew/formula-patches/92d4cf/qt/5.15.2.diff#/libqt-0001-find-11.0-sdk.patch

Patch1:     libqt-0002-export-all-staticmetaobjects.patch

BuildRequires:  libqt-devel
BuildRequires:  qt
Requires:       libqt

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n qt-everywhere-src-%{version} -p1

%ifarch aarch64
sed -e 's/stat64/stat/' -i.orig qt3d/src/3rdparty/assimp/contrib/zip/src/miniz.h
%endif

%build
mkdir build_webengine
cd build_webengine
qmake ../qtwebengine
%make_build

%install
%make_install

%files

%changelog
