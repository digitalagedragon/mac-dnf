%define libname openssl

Name:           lib%{libname}
Version:        1.1.1i
Release:        3%{?dist}
Summary:        OpenSSL is a robust, commercial-grade, and full-featured toolkit for the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) protocols.

License:        OpenSSL
URL:            https://www.openssl.org/
%undefine       _disable_source_fetch
Source0:        https://www.openssl.org/source/%{libname}-%{version}.tar.gz
%define         SHA256SUM0 e8be6a35fe41d10603c3cc635e93289ed00bf34b79671a3a4de64fcee00d5242

# X10-Update-Spec: { "type": "webscrape",
# X10-Update-Spec:   "url": "https://www.openssl.org/source/",
# X10-Update-Spec:   "pattern": "(?:href=\"|/)\\w+-((?:\\d+\\.)*\\d+.?)\\.tar\\..z2?\"" }

%undefine _annotated_build
%global debug_package %{nil}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package     -n openssl
Summary:        Command-line utilities for libopenssl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n openssl

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version}

%build

./config \
    --prefix=%{_prefix} --libdir=lib \
    --openssldir=%{_sysconfdir}/ssl shared zlib-dynamic
%make_build

%install
%make_install MANSUFFIX=ssl

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%{__install} -dm755 %{buildroot}%{_prefix}/opt/%{name}
mv -v %{buildroot}%{_bindir} %{buildroot}%{_prefix}/opt/%{name}/

%posttrans -n openssl
echo Note: macOS provides its own openssl, so %{name}\\'s binaries have been installed under /usr/local/opt/%{name}/bin.

%files
%license LICENSE
%{_sysconfdir}/ssl
# this gets installed as empty and would conflict with p11-kit
%exclude %{_sysconfdir}/ssl/certs
%{_prefix}/lib/libcrypto.*.dylib
%{_prefix}/lib/libssl.*.dylib
%{_prefix}/lib/engines-1.1
%doc %{_mandir}/man{5,7}/*

%files devel
%{_includedir}/openssl
%{_prefix}/lib/libcrypto.dylib
%{_prefix}/lib/libssl.dylib
%{_prefix}/lib/*.a
%{_prefix}/lib/pkgconfig/*.pc
%doc %{_mandir}/man3/*
# TODO this probably should get split too - have one package
# own the dir
%doc %{_datadir}/doc/openssl

%files -n openssl
%{_prefix}/opt/%{name}/bin/c_rehash
%{_prefix}/opt/%{name}/bin/openssl
%doc %{_mandir}/man1/*

%changelog

* Thu Dec 31 2020 Morgan Thomas <m@m0rg.dev> 1.1.1i-3
  Move binaries to /usr/local/opt.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.1.1i-2
  Rebuilt with dependency generation.
