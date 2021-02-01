Name:           asciidoc
Version:        9.0.5
Release:        1%{?dist}
Summary:        An ASCII-based markup format

License:        GPLv2+
URL:            https://asciidoc.org/
%undefine       _disable_source_fetch
Source0:        https://github.com/asciidoc/asciidoc-py3/releases/download/%{version}/%{name}-%{version}.tar.gz
%define         SHA256SUM0 1a20647eb62ca37bc8107affab968caa0f674f0e962b497d1674391f636c7038

BuildArch:      noarch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/asciidoc/asciidoc-py3.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup
sed -e '/^XMLLINT/s/xmllint//' -i.orig a2x.py

%build
%configure
%make_build

%install
%make_install

%files
%license COPYRIGHT
%{_bindir}/*
%{_sysconfdir}/asciidoc
%doc %{_mandir}/man1/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 9.0.5-1
  Updated to version 9.0.5.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 9.0.4-2
  Rebuilt with dependency generation.
