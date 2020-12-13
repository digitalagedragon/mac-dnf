%define libname zchunk

Name:           lib%{libname}
Version:        1.1.7
Release:        1%{?dist}
Summary:        zchunk is a compressed file format that splits the file into independent chunks

License:        BSD-2-Clause
URL:            https://github.com/zchunk/zchunk
%undefine       _disable_source_fetch
Source0:        https://github.com/zchunk/%{libname}/archive/%{version}.tar.gz#/%{libname}-%{version}.tar.gz
%define         SHA256SUM0 eb3d531916d6fea399520a2a4663099ddbf2278088599fa09980631067dc9d7b

Patch0:         libzchunk-0001-endian-h.patch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/zchunk/zchunk.git",
# X10-Update-Spec:   "pattern": "^((?:\\d+\\.?)+)$" }

BuildRequires:  meson ninja-build

BuildRequires:  libopenssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  libzstd-devel
BuildRequires:  libargp-devel

Requires: libcurl libopenssl

%undefine _annotated_build
%global debug_package %{nil}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libffi-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n zchunk
Summary:        Command-line utilities for libzchunk
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n zchunk

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version} -p0

%build

mkdir build
LDFLAGS=-largp meson -Dbuildtype=release --prefix=%{_prefix} build/
ninja %{?_smp_mflags} -C build

%install
DESTDIR=%{buildroot} ninja -C build install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license LICENSE
%{_prefix}/lib/libzck.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libzck.dylib
%{_prefix}/lib/pkgconfig/*.pc

%files -n zchunk
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
