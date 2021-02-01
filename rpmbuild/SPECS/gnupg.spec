Name:           gnupg
Version:        2.2.27
Release:        1%{?dist}
Summary:        The GNU Privacy Guard

License:        GPLv2+
URL:            https://www.gnupg.org/
%undefine       _disable_source_fetch
Source0:        https://www.gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
%define         SHA256SUM0 34e60009014ea16402069136e0a5f63d9b65f90096244975db5cea74b3d02399

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.gnupg.org/ftp/gcrypt/gnupg"}

BuildRequires:  libgpg-error-devel
BuildRequires:  libnpth-devel
BuildRequires:  pkgconfig(ksba)
BuildRequires:  pkgconfig(libassuan)
BuildRequires:  pkgconfig(libgcrypt)

Recommends:     pinentry

Requires:       libassuan
Requires:       libgpg-error
Requires:       libgcrypt
Requires:       libksba
Requires:       libnpth

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%configure --libdir=%{_prefix}/lib
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir

%find_lang gnupg2

%files -f gnupg2.lang
%license COPYING
%{_bindir}/dirmngr
%{_bindir}/dirmngr-client
%{_bindir}/gpg
%{_bindir}/gpg-agent
%{_bindir}/gpg-connect-agent
%{_bindir}/gpg-wks-server
%{_bindir}/gpgconf
%{_bindir}/gpgparsemail
%{_bindir}/gpgscm
%{_bindir}/gpgsm
%{_bindir}/gpgsplit
%{_bindir}/gpgtar
%{_bindir}/gpgv
%{_bindir}/kbxutil
%{_bindir}/watchgnupg
%{_sbindir}/*
%{_libexecdir}/*
%{_datadir}/gnupg/distsigkey.gpg
%{_datadir}/gnupg/sks-keyservers.netCA.pem
%doc %{_infodir}/*.info*
%doc %{_mandir}/man{1,7,8}/*
%doc %{_datadir}/gnupg/*.txt
%doc %{_datadir}/doc/gnupg

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 2.2.27-1
  Updated to version 2.2.27.

* Mon Dec 28 2020 Morgan Thomas <m@m0rg.dev> 2.2.26-3
  Use pkgconfig dependencies.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 2.2.26-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 2.2.26-1
  Updated to version 2.2.26.

* Wed Dec 16 2020 Morgan Thomas <m@m0rg.dev> 2.2.25 release 2
  Added run-time dependencies.
