%define libname check

Name:           lib%{libname}
Version:        0.15.2
Release:        3%{?dist}
Summary:        Check is a unit testing framework for C.

License:        LGPLv2
URL:            https://libcheck.github.io/check/
%undefine       _disable_source_fetch
Source0:        https://github.com/libcheck/%{libname}/releases/download/%{version}/%{libname}-%{version}.tar.gz
%define         SHA256SUM0 a8de4e0bacfb4d76dd1c618ded263523b53b85d92a146d8835eb1a52932fa20a

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/libcheck/check.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+\\.\\d+)$" }

BuildRequires:  autoconf automake libtool
BuildRequires:  pkgconfig(libpkgconf)

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package     -n checkmk
Summary:        Script for generating unit tests for use with libcheck
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n checkmk

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version}
export PATH=%{_prefix}/opt/libtool/bin:$PATH
autoreconf --install

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
%license COPYING.LESSER
%{_prefix}/lib/libcheck.*.dylib
%doc %{_infodir}/*.info*

%files devel
%{_includedir}/*
%{_prefix}/lib/libcheck.dylib
%{_datadir}/aclocal/*.m4
%{_prefix}/lib/pkgconfig/*.pc
%doc %{_datadir}/doc/check

%files -n checkmk
%{_bindir}/checkmk
%doc %{_mandir}/man1/*

%changelog

* Mon Dec 28 2020 Morgan Thomas <m@m0rg.dev> 0.15.2-3
  Use pkgconfig dependencies.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 0.15.2-2
  Rebuilt with dependency generation.
