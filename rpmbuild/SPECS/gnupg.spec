Name:           gnupg
Version:        2.2.25
Release:        1%{?dist}
Summary:        The GNU Privacy Guard

License:        GPLv2+
URL:            https://www.gnupg.org/
%undefine       _disable_source_fetch
Source0:        https://www.gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
%define         SHA256SUM0 c55307b247af4b6f44d2916a25ffd1fb64ce2e509c3c3d028dbe7fbf309dc30a

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.gnupg.org/ftp/gcrypt/gnupg"}

BuildRequires:  pkg-config
BuildRequires:  libassuan-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libksba-devel
BuildRequires:  libnpth-devel

Recommends:     pinentry

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
