Name:           node
Version:        15.5.0
Release:        3%{?dist}
Summary:        An asynchronous JavaScript runtime

License:        MIT
URL:            https://nodejs.org
%undefine       _disable_source_fetch
Source0:        https://nodejs.org/dist/v%{version}/node-v%{version}.tar.gz
%define         SHA256SUM0 a4f10a2e67dc99ed64c297be988fbe37f8a62f8fb8ff880f121f8be4e30df3d1

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

* Sun Dec 27 2020 Morgan Thomas <m@m0rg.dev> 15.5.0-3
  Rebuilt for libtool -> glibtool.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 15.5.0-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 15.5.0-1
  Updated to version 15.5.0.
