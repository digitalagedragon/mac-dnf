Name:           curl
Version:        7.74.0
Release:        4%{?dist}
Summary:        Curl is a command line tool and library for transferring data with URLs.

License:        libcurl
URL:            https://curl.haxx.se/
%undefine       _disable_source_fetch
Source0:        https://curl.haxx.se/download/%{name}-%{version}.tar.xz
%define         SHA256SUM0 999d5f2c403cf6e25d58319fdd596611e455dd195208746bc6e6d197a77e878b

# X10-Update-Spec: { "type": "webscrape", "url": "https://curl.haxx.se/download/"}

BuildRequires:  pkgconfig(libssl)

Requires:       libcurl = %{version}-%{release}

%undefine _annotated_build
%global debug_package %{nil}

%description

%package     -n libcurl
Summary:        libcurl is a free and easy-to-use client-side URL transfer library.
License:        libcurl
URL:            https://curl.haxx.se/

%description -n libcurl

%package     -n libcurl-devel
Summary:        Development files for libcurl
Requires:       libcurl%{?_isa} = %{version}-%{release}

%description -n libcurl-devel
The libcurl-devel package contains libraries and header files for
developing applications that use libcurl.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version}

%build
%configure --bindir=%{_prefix}/opt/%{name}/bin --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%posttrans
echo Note: macOS provides its own %{name}, so %{name}\\'s binaries have been installed under /usr/local/opt/%{name}/bin.

%files
%license COPYING
%{_prefix}/opt/%{name}/bin/*
%doc %{_mandir}/man1/*

%files -n libcurl
%{_prefix}/lib/libcurl.*.dylib

%files -n libcurl-devel
%{_includedir}/curl
%{_prefix}/lib/libcurl.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%doc %{_mandir}/man3/*

%changelog

* Thu Dec 31 2020 Morgan Thomas <m@m0rg.dev> 7.74.0-4
  Move binaries to /usr/local/opt.

* Mon Dec 28 2020 Morgan Thomas <m@m0rg.dev> 7.74.0-3
  Use pkgconfig dependencies.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 7.74.0-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 7.74.0-1
  Updated to version 7.74.0.
