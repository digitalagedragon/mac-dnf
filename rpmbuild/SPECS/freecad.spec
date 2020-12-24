%define system_python 3.9

Name:           freecad
Version:        0.19pre
Release:        2%{?dist}
Summary:        Parametric 3D modeler

License:        GPLv2
URL:            http://www.freecadweb.org
%undefine       _disable_source_fetch
# this is freecad's own "Known Good" 0.19pre commit (https://github.com/FreeCAD/homebrew-freecad/blob/master/Formula/freecad.rb)
%define source_commit f35d30bc58cc2000754d4f30cf29d063416cfb9e
Source0:        https://github.com/freecad/freecad/archive/%{source_commit}.tar.gz#/freecad-0.19pre.tar.gz

Patch0:         freecad-0001-homebrew-paths.patch
Patch1:         freecad-0002-skip-macos-package-manager-check.patch
Patch2:         freecad-0003-qt-paths.patch

# RPM-Audit-Skip Audit::SHA256Present

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  libboost-devel
BuildRequires:  libcoin-devel
BuildRequires:  libeigen-devel
BuildRequires:  libicu4c-devel
BuildRequires:  libnetgen-devel
BuildRequires:  libopencascade-devel
BuildRequires:  libpython%{system_python}-devel
BuildRequires:  libqt-devel
BuildRequires:  libxerces-c-devel
BuildRequires:  pivy
BuildRequires:  pkg-config
BuildRequires:  pyside2-devel
BuildRequires:  python%{system_python}
BuildRequires:  qt
BuildRequires:  shiboken2-devel
BuildRequires:  swig

Requires:       libboost
Requires:       libcoin
Requires:       libeigen
Requires:       libicu4c
Requires:       libnetgen
Requires:       libopencascade
Requires:       libqt
Requires:       libxerces-c
Requires:       pivy
Requires:       pyside2
Requires:       shiboken2
%description

%prep
%autosetup -n FreeCAD-%{source_commit} -p0

# can't do this with patch due to CRLF nonsense
sed -i.orig -e 's/!defined(__x86_64__)/0/' src/Mod/Mesh/App/WildMagic4/Wm4System.cpp

%build
mkdir build
cd build

# TODO: build OpenSCAD integration 'cause it's useful
# TODO: -DOCCT_CMAKE_FALLBACK=ON is due to libopencascade problems, I think
# TODO: -DBUILD_WEB=1 requires qtwebengine
# TODO: -DBUILD_FEM_NETGEN=1 requires VTK

%cmake_configure \
      -DBUILD_QT5=ON \
      -DUSE_PYTHON3=1 \
      -DPYTHON_EXECUTABLE=/usr/local/bin/python%{system_python} \
      -std=c++14 \
      -DCMAKE_CXX_STANDARD=14 \
      -DBUILD_ENABLE_CXX_STD:STRING=C++14 \
      -DBUILD_FEM_NETGEN=0 \
      -DBUILD_FEM=0 \
      -DBUILD_WEB=0 \
      -DBUILD_FEM_NETGEN:BOOL=OFF \
      -DFREECAD_USE_EXTERNAL_KDL=OFF \
      -DOCCT_CMAKE_FALLBACK=ON \
      -DFREECAD_CREATE_MAC_APP=1 \
      ..
%cmake_build || cmake --build . --verbose

%install
cd build
%make_install

%{__install} -dm755 %{buildroot}%{_bindir}/
%{__install} -dm755 %{buildroot}/Applications
mv -v %{buildroot}%{_prefix}/FreeCAD.app %{buildroot}%{_bindir}/
ln -sfv /usr/local/lib/python%{system_python} %{buildroot}%{_bindir}/FreeCAD.app/Contents/lib/
ln -sfv %{_bindir}/FreeCAD.app %{buildroot}/Applications/FreeCAD.app

# apparently the bundle doesn't come out relocatable enough
install_name_tool -rpath %{_prefix}/FreeCAD.app/Contents/lib @executable_path/../lib %{buildroot}%{_bindir}/FreeCAD.app/Contents/MacOS/FreeCAD
install_name_tool -rpath %{_prefix}/FreeCAD.app/Contents/lib @executable_path/../lib %{buildroot}%{_bindir}/FreeCAD.app/Contents/MacOS/FreeCADCmd

# this may be indicative of larger Qt problems but I really have no idea
cat >%{buildroot}%{_bindir}/FreeCAD.app/Contents/Resources/qt.conf <<EOF
[Paths]
Plugins = /usr/local/share/plugins
EOF

%files
%{_bindir}/FreeCAD.app
/Applications/FreeCAD.app

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 0.19pre-2
  Rebuilt with dependency generation.
