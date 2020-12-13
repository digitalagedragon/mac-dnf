%define libname cppunit

Name:           lib%{libname}
Version:        1.15.1
Release:        1%{?dist}
Summary:        CppUnit is the C++ port of the famous JUnit framework for unit testing.

License:        LGPLv2
URL:            https://www.freedesktop.org/wiki/Software/cppunit/
%undefine       _disable_source_fetch
Source0:        http://dev-www.libreoffice.org/src/%{libname}-%{version}.tar.gz
%define         SHA256SUM0 89c5c6665337f56fd2db36bc3805a5619709d51fb136e51937072f63fcc717a7

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.freedesktop.org/wiki/Software/cppunit/"}

%undefine _annotated_build
%global debug_package %{nil}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version}

%build

mkdir build
cd build
%define _configure ../configure
%configure --libdir=%{_prefix}/lib --disable-static
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%exclude %{_bindir}/*
%{_prefix}/lib/libcppunit-*.dylib
%doc %{_datadir}/doc/%{libname}

%files devel
%{_includedir}/*
%{_prefix}/lib/libcppunit.dylib
%{_prefix}/lib/pkgconfig/*.pc

%changelog
