%ifarch aarch64
%define universal() %{1}-universal
%else
%define universal() %{1}
%endif

Name:           qemu
Version:        5.2.0
Release:        2%{?dist}
Summary:        Open-source machine emulator and virtualizer

License:        GPLv2, LGPLv2
URL:            https://qemu.org
%undefine       _disable_source_fetch
Source0:        https://download.qemu.org/qemu-%{version}.tar.xz
%define         SHA256SUM0 cb18d889b628fbe637672b0326789d9b0e3b8027e0445b936537c78549df17bc

# X10-Update-Spec: { "type": "webscrape", "url": "https://download.qemu.org/"}

BuildRequires:  xz
BuildRequires:  ninja-build
BuildRequires:  pkg-config
BuildRequires:  %{universal glib2}-devel
BuildRequires:  %{universal libpixman}-devel
BuildRequires:  %{universal libintl}

Requires:       %{universal glib2}
Requires:       %{universal libpixman}
Requires:       %{universal libintl}

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version} -p0

%build

# no hvf on aarch64. this will build x86_64 binaries for both platforms
%ifarch aarch64
export CFLAGS="-arch x86_64"
export CXXFLAGS="-arch x86_64"
export LDFLAGS="-arch x86_64"
%endif

# qemu's configure is not autoconf
./configure --prefix=%{_prefix}
%make_build

%install
%make_install

%files
%license COPYING COPYING.LIB
%{_bindir}/qemu-img
%{_bindir}/qemu-edid
%{_bindir}/qemu-ga
%{_bindir}/qemu-io
%{_bindir}/qemu-nbd
%{_bindir}/qemu-storage-daemon
%{_bindir}/elf2dmp
%{_bindir}/qemu-system-*
%{_datadir}/qemu
%exclude %{_datadir}/icons
%exclude %{_datadir}/applications

%changelog
