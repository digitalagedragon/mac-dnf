%define libname libmpc

Name:           %{libname}
Version:        1.2.1
Release:        2%{?dist}
Summary:        GNU MPC is a C library for the arithmetic of complex numbers with arbitrarily high precision and correct rounding of the result.

License:        LGPLv3+
URL:            http://www.multiprecision.org/mpc/home.html
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/mpc/mpc-%{version}.tar.gz
%define         SHA256SUM0 17503d2c395dfcf106b622dc142683c1199431d095367c6aacba6eec30340459

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/mpc/"}

BuildRequires:  libgmp-devel
BuildRequires:  libmpfr-devel

Requires:       libgmp
Requires:       libmpfr

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n mpc-%{version}

%build

mkdir build
cd build
%define _configure ../configure
%configure --disable-static
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING.LESSER
%{_prefix}/lib/libmpc.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libmpc.dylib
%doc %{_infodir}/mpc.info*

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.2.1-2
  Rebuilt with dependency generation.
