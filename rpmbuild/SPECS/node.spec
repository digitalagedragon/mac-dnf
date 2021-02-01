Name:           node
Version:        15.6.0
Release:        1%{?dist}
Summary:        An asynchronous JavaScript runtime

License:        MIT
URL:            https://nodejs.org
%undefine       _disable_source_fetch
Source0:        https://nodejs.org/dist/v%{version}/node-v%{version}.tar.gz
%define         SHA256SUM0 1dd3681e85bb9c8205a331bfac5121050893defb5ad9d04698239aeef4e736b3

# X10-Update-Spec: { "type": "webscrape", "url": "https://nodejs.org/en/", "pattern": "((?:\\d+\\.?)+) Current"}

BuildRequires:  python
# apparently this is not sufficient to have it not use its own openssl? TODO
BuildRequires:  libopenssl-devel
BuildRequires:  pkg-config
BuildRequires:  glibtool

Requires:       libopenssl

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n node-v%{version}

%build
LIBTOOL=glibtool ./configure --prefix=%{_prefix}
%make_build

%install
%make_install

%files
%license LICENSE
%{_bindir}/node
%{_bindir}/npm
%{_bindir}/npx
%{_libdir}/node_modules
%{_libdir}/dtrace/node.d
%{_includedir}/node
%{_datadir}/systemtap/tapset/node.stp
%doc %{_docdir}/node
%doc %{_mandir}/man1/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 15.6.0-1
  Updated to version 15.6.0.

* Wed Jan 06 2021 Morgan Thomas <m@m0rg.dev> 15.5.1-1
  Updated to version 15.5.1.

* Sun Dec 27 2020 Morgan Thomas <m@m0rg.dev> 15.5.0-3
  Rebuilt for libtool -> glibtool.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 15.5.0-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 15.5.0-1
  Updated to version 15.5.0.
