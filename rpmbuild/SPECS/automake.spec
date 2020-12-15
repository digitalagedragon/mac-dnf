Name:           automake
Version:        1.16.3
Release:        1%{?dist}
Summary:        another giant pile of m4

License:        GPLv3+
URL:            https://gnu.org/software/automake
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
%define         SHA256SUM0 ce010788b51f64511a1e9bb2a1ec626037c6d0e7ede32c1c103611b9d3cba65f
BuildArch:      noarch

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/automake/"}

BuildRequires:  autoconf

Requires:       autoconf

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
%{_datadir}/aclocal-%(echo %{version} | sed -E 's/\.[0-9]+$//')
%{_datadir}/automake-%(echo %{version} | sed -E 's/\.[0-9]+$//')

%doc %{_datadir}/doc/automake
%doc %{_datadir}/aclocal/README
%doc %{_infodir}/*.info*
%doc %{_mandir}/man1/*

%changelog
