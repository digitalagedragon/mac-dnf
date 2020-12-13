Name:           libffi
Version:        3.3
Release:        1%{?dist}
Summary:        The libffi library provides a portable, high level programming interface to various calling conventions.

License:        MIT
URL:            https://github.com/libffi/libffi/
%undefine       _disable_source_fetch
Source0:        https://github.com/libffi/%{name}/archive/v%{version}.tar.gz#/libffi-%{version}.tar.gz
%define         SHA256SUM0 3f2f86094f5cf4c36cfe850d2fe029d01f5c2c2296619407c8ba0d8207da9a6b

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/libffi/libffi.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

BuildRequires:  make autoconf automake libtool

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version}
./autogen.sh

%build

mkdir build
cd build
%define _configure ../configure
%configure \
%ifarch aarch64
    --build=aarch64-apple-darwin%(uname -r) \
    --host=aarch64-apple-darwin%(uname -r) \
    --target=aarch64-apple-darwin%(uname -r) \
%endif
    --libdir=%{_prefix}/lib --disable-static --disable-debug --disable-dependency-tracking
%make_build

%install
cd build
%make_install

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
