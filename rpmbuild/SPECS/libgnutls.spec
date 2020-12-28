%define major_version 3.6
%define patch_version 15

Name:           libgnutls
Version:        %{major_version}.%{patch_version}
Release:        1%{?dist}
Summary:        The GNU Transport Layer Security library

License:        GPLv3, LGPLv2+
URL:            https://gnutls.org/
%undefine       _disable_source_fetch
Source0:        https://www.gnupg.org/ftp/gcrypt/gnutls/v%{major_version}/gnutls-%{version}.tar.xz
%define         SHA256SUM0 0ea8c3283de8d8335d7ae338ef27c53a916f15f382753b174c18b45ffd481558

BuildRequires:  xz
BuildRequires:  libgmp-devel
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  libunistring-devel

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n gnutls
Summary:        Command-line tools and utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n gnutls

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n gnutls-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fv %{buildroot}%{_infodir}/dir

%find_lang gnutls

%files -f gnutls.lang
%{_libdir}/libgnutls.*.dylib
%{_libdir}/libgnutlsxx.*.dylib

%files devel
%{_includedir}/gnutls
%{_libdir}/libgnutls.dylib
%{_libdir}/libgnutlsxx.dylib
%{_libdir}/pkgconfig/gnutls.pc
%{_mandir}/man3/*
%{_docdir}/gnutls
%{_infodir}/*

%files -n gnutls
%{_bindir}/*
%{_mandir}/man1/*

%changelog
