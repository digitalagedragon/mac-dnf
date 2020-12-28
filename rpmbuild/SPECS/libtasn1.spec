Name:           libtasn1
Version:        4.16.0
Release:        1%{?dist}
Summary:        ASN.1 parsing library

License:        LGPLv2+
URL:            https://www.gnu.org/software/libtasn1/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/libtasn1/libtasn1-%{version}.tar.gz
%define         SHA256SUM0 0e0fb0903839117cb6e3b56e68222771bebf22ad7fc2295a0ed7d576e8d4329d

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n tasn1
Summary:        Command-line tools and utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n tasn1

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fv %{buildroot}%{_infodir}/dir

%files
%{_libdir}/libtasn1.*.dylib

%files devel
%{_libdir}/libtasn1.dylib
%{_libdir}/pkgconfig/libtasn1.pc
%{_includedir}/libtasn1.h
%{_mandir}/man3/*
%{_infodir}/*

%files -n tasn1
%{_bindir}/asn1Coding
%{_bindir}/asn1Decoding
%{_bindir}/asn1Parser
%{_mandir}/man1/*

%changelog
