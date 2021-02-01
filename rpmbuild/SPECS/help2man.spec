Name:           help2man
Version:        1.47.17
Release:        1%{?dist}
Summary:        Generates man pages from --help output

License:        GPLv3+
URL:            https://gnu.org/software/help2man
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
%define         SHA256SUM0 da3a35c50b1e1f8c8fa322d69fa47c9011ce443a8fb8d1d671b1f01b8b0008eb

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/help2man/"}

BuildArch:      noarch

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/*
%doc %{_infodir}/*.info*
%doc %{_mandir}/man1/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 1.47.17-1
  Updated to version 1.47.17.
