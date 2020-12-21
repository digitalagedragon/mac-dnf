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

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/mpc/"}

BuildRequires:  xz
BuildRequires:  libgmp-devel
BuildRequires:  libmpfr-devel
BuildRequires:  libmpc-devel

Requires:       libgmp
Requires:       libmpfr
Requires:       libmpc

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

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
    --enable-checking=release \
    --disable-multilib \
    --with-system-zlib \
    SED=/usr/bin/sed

%make_build BOOT_LDFLAGS=-Wl,-headerpad_max_install_names

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING

%changelog
