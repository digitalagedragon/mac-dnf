%define libname npth

Name:           lib%{libname}
Version:        1.6
Release:        2%{?dist}
Summary:        The New Portable Threads Library

License:        LGPLv2+
URL:            https://www.gnupg.org/
%undefine       _disable_source_fetch
Source0:        https://www.gnupg.org/ftp/gcrypt/%{libname}/%{libname}-%{version}.tar.bz2
%define         SHA256SUM0 1393abd9adcf0762d34798dc34fdcf4d0d22a8410721e76f1e3afcd1daa4e2d1

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.gnupg.org/ftp/gcrypt/npth"}

BuildRequires:  libgpg-error-devel 
BuildRequires:  pkg-config

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
%configure --libdir=%{_prefix}/lib
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING.LIB
%{_prefix}/lib/libnpth.*.dylib

%files devel
%{_prefix}/bin/npth-config
%{_includedir}/*
%{_prefix}/lib/libnpth.dylib
%{_datadir}/aclocal/*.m4

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.6-2
  Rebuilt with dependency generation.

