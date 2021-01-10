Name:           wget
Version:        1.21
Release:        1%{?dist}
Summary:        Internet file retriever

License:        GPLv3+
URL:            https://www.gnu.org/software/wget/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/wget/wget-%{version}.tar.gz
%define         SHA256SUM0 b3bc1a9bd0c19836c9709c318d41c19c11215a07514f49f89b40b9d50ab49325

BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(gnutls)

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

patch -p1 <<EOF
--- a/lib/utime.c
+++ b/lib/utime.c
@@ -261,6 +261,7 @@ utime (const char *name, const struct utimbuf *ts)
 
 #else
 
+# include <errno.h>
 # include <sys/stat.h>
 # include "filename.h"
EOF

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
