Name:           libnettle
Version:        3.6
Release:        1%{?dist}
Summary:        A low-level cryptographic library

License:        GPLv2+, LGPLv3+
URL:            https://www.lysator.liu.se/~nisse/nettle/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/nettle/nettle-%{version}.tar.gz
%define         SHA256SUM0 d24c0d0f2abffbc8f4f34dcf114b0f131ec3774895f3555922fe2f40f3d5e3f1

BuildRequires:  libgmp-devel

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n nettle
Summary:        Command-line tools and utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n nettle

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n nettle-%{version}

%build
%configure \
%ifarch aarch64
    --disable-assembler \
%endif
    --enable-shared \
    --disable-static

%make_build

%install
%make_install

rm -fv %{buildroot}%{_infodir}/dir

%files
%{_libdir}/libhogweed.*.dylib
%{_libdir}/libnettle.*.dylib

%files devel
%{_includedir}/nettle
%{_libdir}/libhogweed.dylib
%{_libdir}/libnettle.dylib
%{_libdir}/pkgconfig/*.pc

%files -n nettle
%{_bindir}/nettle-hash
%{_bindir}/nettle-lfib-stream
%{_bindir}/nettle-pbkdf2
%{_bindir}/pkcs1-conv
%{_bindir}/sexp-conv
%{_infodir}/*
%changelog
