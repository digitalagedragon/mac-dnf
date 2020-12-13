Name:           autoconf
Version:        2.69
Release:        1%{?dist}
Summary:        makes all those configure scripts

License:        GPLv3+
URL:            https://gnu.org/software/autoconf
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
%define         SHA256SUM0 954bd69b391edc12d6a4a51a2dd1476543da5c6bbf05a95b59dc0dd6fd4c2969

BuildArch:      noarch

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/autoconf/"}

BuildRequires:  make
BuildRequires:  m4
BuildRequires:  perl

Requires:       m4

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING
%{_bindir}/*
%{_datadir}/autoconf
%doc %{_infodir}/*.info*
%doc %{_mandir}/man1/*

%changelog
