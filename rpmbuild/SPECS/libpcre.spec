%enable_universal

%define libname pcre

Name:           %{universal lib%{libname}}
Version:        8.44
Release:        4%{?dist}
Summary:        Perl Compatible Regular Expressions

License:        BSD
URL:            https://pcre.org
%undefine       _disable_source_fetch
Source0:        https://ftp.pcre.org/pub/pcre/%{libname}-%{version}.tar.bz2
%define         SHA256SUM0 19108658b23b3ec5058edc9f66ac545ea19f9537234be1ec62b714c84399366d

# X10-Update-Spec: { "type": "webscrape",
# X10-Update-Spec:   "url": "https://ftp.pcre.org/pub/pcre/",
# X10-Update-Spec:   "pattern": "(?:href=\"|/)\\w+-(\\d\\.(?:\\d+\\.)*\\d+)\\.tar\\..z2?\"" }

%uprovides libpcre

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%uprovides libpcre devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n %{universal pcre}
Summary:        Command-line utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%uprovides pcre

%description -n %{universal pcre}

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version}

%build

%ufor
%configure --libdir=%{_prefix}/lib --disable-static
%make_build
%udone

%install
%uinstall

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license LICENCE
%{_prefix}/lib/libpcre.*.dylib
%{_prefix}/lib/libpcrecpp.*.dylib
%{_prefix}/lib/libpcreposix.*.dylib

%files devel
%{_bindir}/pcre-config
%{_includedir}/*
%{_prefix}/lib/libpcre.dylib
%{_prefix}/lib/libpcrecpp.dylib
%{_prefix}/lib/libpcreposix.dylib
%{_prefix}/lib/pkgconfig/*.pc
%doc %{_datadir}/doc/pcre
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/pcre-config.1*

%files -n %{universal pcre}
%{_bindir}/pcretest
%{_bindir}/pcregrep
%doc %{_mandir}/man1/pcregrep.1*
%doc %{_mandir}/man1/pcretest.1*

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 8.44-4
  Rebuilt with dependency generation.
