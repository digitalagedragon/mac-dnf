Name:           libgpg-error
Version:        1.39
Release:        1%{?dist}
Summary:        Libgpg-error is a small library that originally defined common error values for all GnuPG components.

License:        LGPLv2+
URL:            https://gnupg.org/software/libgpg-error/index.html
%undefine       _disable_source_fetch
Source0:        https://gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
%define         SHA256SUM0 4a836edcae592094ef1c5a4834908f44986ab2b82e0824a0344b49df8cdb298f

# X10-Update-Spec: { "type": "webscrape",
# X10-Update-Spec:   "url": "https://gnupg.org/ftp/gcrypt/libgpg-error",
# X10-Update-Spec:   "pattern": "(?:href=\"|/)libgpg-error-((?:\\d+\\.)*\\d+)\\.tar\\..z2?\""}

BuildRequires:  make clang

%undefine _annotated_build
%global debug_package %{nil}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n gpg-error
Summary:        Utility programs for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n gpg-error


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version}

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
rm -f %{buildroot}%{_infodir}/dir

%find_lang libgpg-error

%files -f build/libgpg-error.lang
%license COPYING COPYING.LIB
%{_prefix}/lib/libgpg-error.*.dylib

%doc %{_infodir}/*.info*
%doc %{_mandir}/man1/*
%doc %{_datadir}/%{name}/errorref.txt

%files devel
%{_includedir}/*
%{_prefix}/bin/gpg-error-config
%{_prefix}/bin/gpgrt-config
%{_prefix}/lib/libgpg-error.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_datadir}/common-lisp/source/gpg-error

%files -n gpg-error
%{_prefix}/bin/gpg-error
%{_prefix}/bin/yat2m

%changelog