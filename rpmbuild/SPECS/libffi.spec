%enable_universal

Name:           %{universal libffi}
Version:        3.3
Release:        4%{?dist}
Summary:        The libffi library provides a portable, high level programming interface to various calling conventions.

License:        MIT
URL:            https://github.com/libffi/libffi/
%undefine       _disable_source_fetch
Source0:        https://github.com/libffi/libffi/archive/v%{version}.tar.gz#/libffi-%{version}.tar.gz
%define         SHA256SUM0 3f2f86094f5cf4c36cfe850d2fe029d01f5c2c2296619407c8ba0d8207da9a6b

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/libffi/libffi.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

%uprovides libffi

BuildRequires:  autoconf automake libtool

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%uprovides libffi devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version}
./autogen.sh

%build

%ufor
%if %{with universal}
%configure \
    --build=$__linux_arch-apple-darwin%(uname -r) \
    --host=$__linux_arch-apple-darwin%(uname -r) \
    --target=$__linux_arch-apple-darwin%(uname -r) \
    --libdir=%{_prefix}/lib --disable-static --disable-debug --disable-dependency-tracking
%else
%configure \
%ifarch aarch64
    --build=aarch64-apple-darwin%(uname -r) \
    --host=aarch64-apple-darwin%(uname -r) \
    --target=aarch64-apple-darwin%(uname -r) \
%endif
    --libdir=%{_prefix}/lib --disable-static --disable-debug --disable-dependency-tracking
%endif
%make_build -j1
%udone

%install
%uinstall

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fv %{buildroot}%{_infodir}/dir

%files
%license LICENSE
%{_prefix}/lib/libffi.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libffi.dylib
%{_prefix}/lib/pkgconfig/*.pc
%doc %{_mandir}/man3/*
%doc %{_infodir}/*.info*

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.3-4
  Rebuilt with dependency generation.
