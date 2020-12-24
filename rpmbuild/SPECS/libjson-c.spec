%define libname json-c
%define silly_version -20200726

Name:           lib%{libname}
Version:        0.15
Release:        2%{?dist}
Summary:        json-c is a library for creating and reading JSON objects in C.

License:        MIT
URL:            https://github.com/json-c/json-c
%undefine       _disable_source_fetch
Source0:        https://github.com/json-c/%{libname}/archive/%{libname}-%{version}%{silly_version}.tar.gz
%define         SHA256SUM0 4ba9a090a42cf1e12b84c64e4464bb6fb893666841d5843cc5bef90774028882

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/json-c/json-c.git",
# X10-Update-Spec:   "pattern": "^json-c-((?:\\d+\\.?)+)-\\d+$" }

BuildRequires:  cmake

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{libname}-%{version}%{silly_version}

%build

mkdir build
cd build

cmake \
    -DBUILD_STATIC_LIBS=OFF \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..

%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%license COPYING
%{_prefix}/lib/libjson-c.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libjson-c.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_prefix}/lib/cmake/json-c

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 0.15-2
  Rebuilt with dependency generation.
