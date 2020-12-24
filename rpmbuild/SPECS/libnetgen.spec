%define system_cmake 3.19

Name:           libnetgen
Version:        6.2.2010pre
Release:        2%{?dist}
Summary:        C++ CAD/CAM library

# earlier versions don't build on M1
%define upstream_commit 65afc44dccb4b0c7d691aebc6fcb39412235a56b

License:        LGPLv2
URL:            https://ngsolve.org
%undefine       _disable_source_fetch
Source0:        https://github.com/NGSolve/netgen/archive/%{upstream_commit}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 e467394d426cfd550c0c29a4a8e9a92bea2f51c220335838780512db1b59f7b8

BuildRequires:  cmake%{system_cmake}
BuildRequires:  libopencascade-devel

Requires:       libopencascade

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n netgen-%{upstream_commit} -p1

%build

mkdir build
cd build

# this is insistent on installing as an application structure on macOS...
cmake \
    -DUSE_PYTHON=OFF \
    -DUSE_GUI=OFF \
    -DUSE_OCC=ON \
    -DUSE_NATIVE_ARCH=ON \
    -DNG_INSTALL_DIR_BIN=bin \
    -DNG_INSTALL_DIR_LIB=lib \
    -DNG_INSTALL_DIR_RES=share \
    -DNG_INSTALL_DIR_INCLUDE=include/netgen \
    -DNG_INSTALL_DIR_CMAKE=lib/cmake/netgen \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..

%make_build

%install
cd build
%make_install

rm -fv %{buildroot}%{_prefix}/Info.plist
rm -fv %{buildroot}%{_prefix}/Netgen.icns

# per https://github.com/FreeCAD/homebrew-freecad/blob/master/Formula/nglib.rb, these aren't
# installed by default
# for subdir in csg general geom2d gprim include interface linalg meshing occ stlgeom visualization; do
#     %{__install} -dm755 %{buildroot}%{_includedir}/netgen/$subdir
#     shopt -s nullglob
#     %{__install} -m644 ../libsrc/$subdir/*{.h,.hpp} %{buildroot}%{_includedir}/netgen/$subdir
#     shopt -u nullglob
# done

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%exclude %{_bindir}
%{_libdir}/*.dylib
# TODO?
%{_libdir}/*.so
%{_datadir}/netgen

%files devel
%{_includedir}/netgen
%{_libdir}/cmake/netgen

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 6.2.2010pre-2
  Rebuilt with dependency generation.

