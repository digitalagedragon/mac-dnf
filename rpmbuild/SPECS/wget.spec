Name:           wget
Version:        1.21.1
Release:        1%{?dist}
Summary:        Internet file retriever

License:        GPLv3+
URL:            https://www.gnu.org/software/wget/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/wget/wget-%{version}.tar.gz
%define         SHA256SUM0 59ba0bdade9ad135eda581ae4e59a7a9f25e3a4bde6a5419632b31906120e26e

# X10-Update-Spec: { "type": "webscrape",
# X10-Update-Spec:   "url": "https://ftp.gnu.org/gnu/wget/",
# X10-Update-Spec:   "exclude": "1\\.99\\.(?:\\d+)" }

BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(gnutls)

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

# stupid GNU extensions again
sed -i.orig 's/__nonnull ((1))//' lib/malloc/dynarray-skeleton.c

%build
%configure \
    --with-ssl=openssl \
    --disable-debug \
    --enable-pcre \
    --disable-pcre2 \
    --without-libpsl

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fv %{buildroot}%{_infodir}/dir

echo 'ca_certificate = /etc/ssl/cert.pem' >> %{buildroot}%{_sysconfdir}/wgetrc

%find_lang wget
%find_lang wget-gnulib

%files -f wget.lang -f wget-gnulib.lang

%{_bindir}/wget
%config %{_sysconfdir}/wgetrc
%{_mandir}/man1/*
%{_infodir}/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 1.21.1-1
  Updated to version 1.21.1.
