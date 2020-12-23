# TODO this doesn't build on aarch64

Name:           gcc
Version:        10.2.0
Release:        1%{?dist}
Summary:        The GNU Compiler Collection

License:        GPLv3
URL:            https://gcc.gnu.org
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-%{version}.tar.xz
%define         SHA256SUM0 b8dd4368bb9c7f0b98188317ee0254dd8cc99d1e3a18d0ff146c855fe16c1d8c

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://gcc.gnu.org/git/gcc.git",
# X10-Update-Spec:   "pattern": "^releases/gcc-(\\d+\\.\\d+\\.\\d+)$" }

Patch0:         https://raw.githubusercontent.com/Homebrew/formula-patches/7baf6e2f/gcc/bigsur.diff#/gcc-0001-bigsur-version-numbering.patch

BuildRequires:  xz
BuildRequires:  libgmp-devel
BuildRequires:  libmpfr-devel
BuildRequires:  libmpc-devel

Requires:       libgmp
Requires:       libmpfr
Requires:       libmpc

Requires:       gcc-libs%{?_isa} = %{version}-%{release}

%description

%package        libs
Summary:        GCC runtime support libraries
License:        GPLv3
URL:            https://gcc.gnu.org

%description    libs

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -p1

%build

mkdir build
cd build
%define _configure ../configure
%configure \
    --disable-nls \
    --enable-checking=release \
    --disable-multilib \
    --with-system-zlib \
    --with-mpc=%{_prefix} \
    --with-mpfr=%{_prefix} \
    --with-gmp=%{_prefix} \
    --enable-languages=c,c++,objc,obj-c++,fortran \
    --with-native-system-header-dir=/usr/include \
    --with-sysroot=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk \
    SED=/usr/bin/sed

%make_build BOOT_LDFLAGS=-Wl,-headerpad_max_install_names

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING
%{_bindir}/*
%{_libexecdir}/gcc/*/%{version}
%{_includedir}/c++/%{version}
%{_libdir}/*.a
%{_libdir}/*.spec
%{_libdir}/gcc/*/%{version}
%{_libdir}/*.py
%{_mandir}/man{1,7}/*
%{_infodir}/*
%{_datadir}/gcc-%{version}

%files libs
%{_libdir}/*.dylib
%{_libdir}/*.so

%changelog
