Name:           libp11-kit
Version:        0.23.22
Release:        1%{?dist}
Summary:        Load and enumerate PKCS#11 modules

License:        BSD-3-Clause
URL:            https://p11-glue.freedesktop.org
%undefine       _disable_source_fetch
Source0:        https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.xz
%define         SHA256SUM0 8a8f40153dd5a3f8e7c03e641f8db400133fb2a6a9ab2aee1b6d0cb0495ec6b6

BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libtasn1)

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n p11-kit
Summary:        Command-line tools and utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n p11-kit

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n p11-kit-%{version}

%build
export FAKED_MODE=1 # https://bugs.freedesktop.org/show_bug.cgi?id=91602#c1
%configure --disable-trust-module
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fv %{buildroot}%{_infodir}/dir

%files
%{_libdir}/libp11-kit.*.dylib
%{_libdir}/p11-kit-proxy.dylib
%{_libdir}/pkcs11
%{_sysconfdir}/pkcs11
%{_libexecdir}/p11-kit

%files devel
%{_includedir}/p11-kit-1
%{_libdir}/libp11-kit.dylib
%{_libdir}/pkgconfig/p11-kit-1.pc
%{_datadir}/gtk-doc/html/p11-kit

%files -n p11-kit
%{_bindir}/p11-kit

%changelog
