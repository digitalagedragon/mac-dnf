%enable_universal

Name:           %{universal libgcrypt}
Version:        1.8.7
Release:        5%{?dist}
Summary:        Libgcrypt is a general purpose cryptographic library originally based on code from GnuPG.

License:        LGPLv2+
URL:            https://gnupg.org/software/libgcrypt/index.html
%undefine       _disable_source_fetch
Source0:        https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
%define         SHA256SUM0 03b70f028299561b7034b8966d7dd77ef16ed139c43440925fe8782561974748

%uprovides libgcrypt

# 1.9.0 held until libdnf update and/or I come up with a better plan for
# rebuilding packages that will break dnf if not updated at once

# X10-Update-Spec: { "type": "webscrape", "url": "https://gnupg.org/ftp/gcrypt/libgcrypt/"}

BuildRequires: %{universal libgpg-error}-devel
BuildRequires: pkg-config

Requires:      libgpg-error

%undefine _annotated_build
%global debug_package %{nil}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{universal libgpg-error}-devel
%uprovides libgcrypt devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n gcrypt
Summary:        Utility programs for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%uprovides gcrypt

%description -n gcrypt

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n libgcrypt-%{version}

%build

%ufor
%configure \
%if %{with universal}
    --build=$__linux_arch-apple-darwin%(uname -r) \
    --host=$__linux_arch-apple-darwin%(uname -r) \
    --target=$__linux_arch-apple-darwin%(uname -r) \
    --disable-asm \
%endif
  --libdir=%{_prefix}/lib
%make_build
%udone

%install
%uinstall

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING COPYING.LIB
%{_prefix}/lib/libgcrypt.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libgcrypt.dylib
%{_datadir}/aclocal/*.m4
%{_prefix}/lib/pkgconfig/*.pc
%{_prefix}/bin/libgcrypt-config
%doc %{_infodir}/*.info*

%files -n gcrypt
%{_prefix}/bin/dumpsexp
%{_prefix}/bin/hmac256
%{_prefix}/bin/mpicalc
%doc %{_mandir}/man1/hmac256.1*

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.8.7-5
  Rebuilt with dependency generation.
