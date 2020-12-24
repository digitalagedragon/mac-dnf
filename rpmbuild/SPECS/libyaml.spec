Name:           libyaml
Version:        0.2.5
Release:        2%{?dist}
Summary:        A C library for parsing and emitting YAML.

License:        MIT
URL:            https://pyyaml.org/wiki/LibYAML
%undefine       _disable_source_fetch
Source0:        http://pyyaml.org/download/%{name}/yaml-%{version}.tar.gz
%define         SHA256SUM0 c642ae9b75fee120b2d96c712538bd2cf283228d2337df2cf2988e3c02678ef4

# X10-Update-Spec: { "type": "webscrape", "url": "http://pyyaml.org/download/libyaml/"}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n yaml-%{version}

%build

mkdir build
cd build
%define _configure ../configure
%configure --libdir=%{_prefix}/lib --disable-static
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license License
%{_prefix}/lib/libyaml-*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libyaml.dylib
%{_prefix}/lib/pkgconfig/*.pc

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 0.2.5-2
  Rebuilt with dependency generation.
