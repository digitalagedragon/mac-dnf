Name:           sed
Version:        4.8
Release:        2%{?dist}
Summary:        GNU sed

License:        GPLv3+
URL:            https://www.gnu.org/software/sed/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/sed/sed-%{version}.tar.xz
%define         SHA256SUM0 f79b0cfea71b37a8eeec8490db6c5f7ae7719c35587f21edb0617f370eeff633

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/sed/"}

Provides:       gsed = %{version}-%{release}

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%configure --bindir=%{_prefix}/opt/%{name}/bin
%make_build

%install
%make_install
rm -fv %{buildroot}%{_infodir}/dir
%find_lang sed

%optlink

%optpost

%files -f sed.lang
%{_bindir}/gsed
%{_prefix}/opt/%{name}/bin/sed
%{_mandir}/man1/*
%{_infodir}/*

%changelog

* Mon Dec 28 2020 Morgan Thomas <m@m0rg.dev> 4.8-2
  Don't pretend to build a -devel package.
