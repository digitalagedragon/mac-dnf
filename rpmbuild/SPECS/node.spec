Name:           node
Version:        15.4.0
Release:        1%{?dist}
Summary:        An asynchronous JavaScript runtime

License:        MIT
URL:            https://nodejs.org
%undefine       _disable_source_fetch
Source0:        https://nodejs.org/dist/v%{version}/node-v%{version}.tar.gz
%define         SHA256SUM0 b199796544d988b4bb61e38584cd097744e073fa0559cbec772858d91ce4649f

# X10-Update-Spec: { "type": "webscrape", "url": "https://nodejs.org/en/", "pattern": "((?:\\d+\\.?)+) LTS"}

BuildRequires:  python
# apparently this is not sufficient to have it not use its own openssl? TODO
BuildRequires:  libopenssl-devel
BuildRequires:  pkg-config

Requires:       libopenssl

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n node-v%{version}

%build
./configure --prefix=%{_prefix}
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
