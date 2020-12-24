%define libname gmp

Name:           lib%{libname}
Version:        6.2.1
Release:        2%{?dist}
Summary:        GMP is a free library for arbitrary precision arithmetic, operating on signed integers, rational numbers, and floating-point numbers.

License:        GPL-2.0-or-later OR LGPL-3.0-or-later
URL:            https://www.gnu.org/software/gmp/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/%{libname}/%{libname}-%{version}.tar.xz
%define         SHA256SUM0 fd4829912cddd12f84181c3451cc752be224643e87fac497b69edddadc49b4f2

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/gmp/"}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version}

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
    --disable-static
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING COPYING.LESSERv3 COPYINGv2 COPYINGv3
%{_prefix}/lib/libgmp.*.dylib
%doc %{_infodir}/*.info*

%files devel
%{_includedir}/*
%{_prefix}/lib/libgmp.dylib
%{_prefix}/lib/pkgconfig/%{libname}.pc

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 6.2.1-2
  Rebuilt with dependency generation.
