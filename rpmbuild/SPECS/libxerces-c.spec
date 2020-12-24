Name:           libxerces-c
Version:        3.2.3
Release:        2%{?dist}
Summary:        Validating XML parser

License:        Apache-2.0
URL:            https://xerces.apache.org/xerces-c/
%undefine       _disable_source_fetch
Source0:        https://archive.apache.org/dist/xerces/c/3/sources/xerces-c-%{version}.tar.gz
%define         SHA256SUM0 fb96fc49b1fb892d1e64e53a6ada8accf6f0e6d30ce0937956ec68d39bd72c7e

BuildRequires:  cmake

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n xerces-c
Summary:        Command-line tools and utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n xerces-c

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n xerces-c-%{version}

%build
mkdir build
cd build
cmake -Wno-dev \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%make_build

# takes absolutely forever
#%check
#cd build
#ctest -V

%install
cd build
%make_install

# per brew - conflicts with `memcached` on case-insensitive fs
rm -fv %{buildroot}%{_bindir}/MemParse

%files
%{_libdir}/libxerces-c-*.dylib

%files devel
%{_includedir}/xercesc
%{_libdir}/cmake/XercesC
%{_libdir}/pkgconfig/xerces-c.pc
%{_libdir}/libxerces-c.dylib
%{_docdir}/xerces-c

%files -n xerces-c
%{_bindir}/*

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.2.3-2
  Rebuilt with dependency generation.
