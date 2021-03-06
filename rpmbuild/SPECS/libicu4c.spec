# adapted from homebrew's

%define major 68
%define minor 2

Name:           libicu4c
Version:        %{major}.%{minor}
Release:        2%{?dist}
Summary:        C/C++ libraries for Unicode and Globalization

License:        ICU
URL:            http://site.icu-project.org/home
%undefine       _disable_source_fetch
Source0:        https://github.com/unicode-org/icu/releases/download/release-%{major}-%{minor}/icu4c-%{major}_%{minor}-src.tgz
%define         SHA256SUM0 c79193dee3907a2199b8296a93b52c5cb74332c26f3d167269487680d479d625

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/unicode-org/icu.git",
# X10-Update-Spec:   "pattern": "^release-(\\d+-\\d+)$" }

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n icu4c
Summary:        Command-line tools and utilities for libicu4c
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n icu4c

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n icu/source -p0

%build
%configure --disable-samples --disable-tests --disable-static --with-library-bits=64
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%{_libdir}/libicudata.*.dylib
%{_libdir}/libicui18n.*.dylib
%{_libdir}/libicuio.*.dylib
%{_libdir}/libicutest.*.dylib
%{_libdir}/libicutu.*.dylib
%{_libdir}/libicuuc.*.dylib

%files devel
%{_libdir}/libicudata.dylib
%{_libdir}/libicui18n.dylib
%{_libdir}/libicuio.dylib
%{_libdir}/libicutest.dylib
%{_libdir}/libicutu.dylib
%{_libdir}/libicuuc.dylib
%{_libdir}/pkgconfig/*.pc
%{_libdir}/icu
%{_includedir}/unicode
%{_datadir}/icu

%files -n icu4c
%{_bindir}/*
%{_sbindir}/*
%doc %{_mandir}/man{1,8}/*

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 68.2-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 68.2-1
  Updated to version 68.2.
