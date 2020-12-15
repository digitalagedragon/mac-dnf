Name:           help2man
Version:        1.47.16
Release:        1%{?dist}
Summary:        Generates man pages from --help output

License:        GPLv3+
URL:            https://gnu.org/software/help2man
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
%define         SHA256SUM0 3ef8580c5b86e32ca092ce8de43df204f5e6f714b0cd32bc6237e6cd0f34a8f4

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
