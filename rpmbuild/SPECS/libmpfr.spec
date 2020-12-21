%define libname mpfr

Name:           lib%{libname}
Version:        4.1.0
Release:        2%{?dist}
Summary:        The MPFR library is a C library for multiple-precision floating-point computations with correct rounding.

License:        LGPLv3+
URL:            https://www.mpfr.org/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/%{libname}/%{libname}-%{version}.tar.xz
%define         SHA256SUM0 0c98a3f1732ff6ca4ea690552079da9c597872d30e96ec28414ee23c95558a7f

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/mpfr/"}

BuildRequires:  libgmp-devel
BuildRequires:  xz

Requires:       libgmp

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
%configure --host=%{_target} --libdir=%{_prefix}/lib --disable-static
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING COPYING.LESSER
%{_prefix}/lib/libmpfr.*.dylib
%doc %{_datadir}/doc/mpfr
%doc %{_infodir}/mpfr.info*

%files devel
%{_includedir}/*
%{_prefix}/lib/libmpfr.dylib
%{_prefix}/lib/pkgconfig/mpfr.pc

%changelog
