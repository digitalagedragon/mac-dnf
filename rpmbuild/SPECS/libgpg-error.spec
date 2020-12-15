%enable_universal

Name:           %{universal libgpg-error}
Version:        1.39
Release:        3%{?dist}
Summary:        Libgpg-error is a small library that originally defined common error values for all GnuPG components.

License:        LGPLv2+
URL:            https://gnupg.org/software/libgpg-error/index.html
%undefine       _disable_source_fetch
Source0:        https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2
%define         SHA256SUM0 4a836edcae592094ef1c5a4834908f44986ab2b82e0824a0344b49df8cdb298f

# X10-Update-Spec: { "type": "webscrape",
# X10-Update-Spec:   "url": "https://gnupg.org/ftp/gcrypt/libgpg-error",
# X10-Update-Spec:   "pattern": "(?:href=\"|/)libgpg-error-((?:\\d+\\.)*\\d+)\\.tar\\..z2?\""}

BuildRequires:  %{universal libintl}

Requires:       %{universal libintl}

%uprovides libgpg-error

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%uprovides libgpg-error devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n %{universal gpg-error}
Summary:        Utility programs for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%uprovides gpg-error

%description -n %{universal gpg-error}


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n libgpg-error-%{version}

%build

%ufor
%configure --libdir=%{_prefix}/lib
%make_build
%udone

%install
%uinstall

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%find_lang libgpg-error

%files -f libgpg-error.lang
%license COPYING COPYING.LIB
%{_prefix}/lib/libgpg-error.*.dylib

%doc %{_infodir}/*.info*
%doc %{_mandir}/man1/*
%doc %{_datadir}/libgpg-error/errorref.txt

%files devel
%{_includedir}/*
%{_prefix}/bin/gpg-error-config
%{_prefix}/bin/gpgrt-config
%{_prefix}/lib/libgpg-error.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_datadir}/common-lisp/source/gpg-error

%files -n %{universal gpg-error}
%{_prefix}/bin/gpg-error
%{_prefix}/bin/yat2m

%changelog