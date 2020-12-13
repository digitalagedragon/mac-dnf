%define libname zstd

Name:           lib%{libname}
Version:        1.4.5
Release:        1%{?dist}
Summary:        A fast lossless compression algorithm

License:        BSD-3-Clause, GPLv2
URL:            https://facebook.github.io/zstd/
%undefine       _disable_source_fetch
Source0:        https://github.com/facebook/zstd/releases/download/v%{version}/zstd-%{version}.tar.gz
%define         SHA256SUM0 98e91c7c6bf162bf90e4e70fdbc41a8188b9fa8de5ad840c401198014406ce9e

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/facebook/zstd.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

BuildRequires:  cmake

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package     -n zstd
Summary:        Command-line utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n zstd

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version}

%build

cd build/cmake
mkdir build
cd build
cmake \
    -DZSTD_BUILD_STATIC=0 \
    -DZSTD_PROGRAMS_LINK_SHARED=1 \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%make_build

%install
cd build/cmake/build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING LICENSE
%{_prefix}/lib/libzstd.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libzstd.dylib
%{_prefix}/lib/cmake/zstd
%{_prefix}/lib/pkgconfig/*.pc

%files -n zstd
%{_bindir}/*
%doc %{_mandir}/man1/*

%changelog
