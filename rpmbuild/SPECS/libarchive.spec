Name:           libarchive
Version:        3.5.1
Release:        1%{?dist}
Summary:        The libarchive project develops a portable, efficient C library that can read and write streaming archives in a variety of formats.

License:        BSD-2-Clause
URL:            https://www.libarchive.org/
%undefine       _disable_source_fetch
Source0:        http://www.libarchive.org/downloads/%{name}-%{version}.tar.gz
%define         SHA256SUM0 9015d109ec00bb9ae1a384b172bf2fc1dff41e2c66e5a9eeddf933af9db37f5a

# X10-Update-Spec: { "type": "webscrape", "url": "http://www.libarchive.org/downloads/"}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n archive
Summary:        Programs from libarchive(3) - bsdtar, mostly

%description -n archive

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version}

%build
%configure --libdir=%{_prefix}/lib --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%{_prefix}/lib/libarchive.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libarchive.dylib
%{_prefix}/lib/pkgconfig/*.pc
%doc %{_mandir}/man{3,5}/*

%files -n archive
%{_bindir}/bsdcat
%{_bindir}/bsdcpio
%{_bindir}/bsdtar
%doc %{_mandir}/man1/*

%changelog

* Sat Dec 26 2020 Morgan Thomas <m@m0rg.dev> 3.5.1-1
  Updated to version 3.5.1.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.4.3-2
  Rebuilt with dependency generation.
