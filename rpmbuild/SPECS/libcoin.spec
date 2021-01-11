%define libname coin

Name:           lib%{libname}
Version:        4.0.0
Release:        2%{?dist}
Summary:        The free and open-source implementation of the Open Inventor API

License:        BSD-3-Clause
URL:            https://coin3d.github.io
%undefine       _disable_source_fetch
Source0:        https://github.com/coin3d/coin/releases/download/Coin-%{version}/coin-%{version}-src.tar.gz
%define         SHA256SUM0 e4f4bd57804b8ed0e017424ad2e45c112912a928b83f86c89963df9015251476

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/coin3d/coin",
# X10-Update-Spec:   "pattern": "^Coin-(\\d+\\.\\d+(?:\\.\\d+)?)$" }

BuildRequires:  cmake
BuildRequires:  cmake3.18
BuildRequires:  libboost-devel

Requires:       libboost

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}

%build

mkdir _build
cd _build
cmake3.18 -Wno-dev \
    -DCOIN_BUILD_MAC_FRAMEWORK=OFF \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}  ..
%make_build

%install
cd _build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%{_libdir}/libCoin.*.dylib
%{_datadir}/Coin

%files devel
%{_bindir}/coin-config
%{_includedir}/Inventor
%{_includedir}/SoDebug.h
%{_includedir}/SoWinEnterScope.h
%{_includedir}/SoWinLeaveScope.h
%{_libdir}/cmake/Coin-%{version}
%{_libdir}/libCoin.dylib
%{_libdir}/pkgconfig/*.pc
%doc %{_infodir}/Coin4

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 4.0.0-2
  Rebuilt with dependency generation.

