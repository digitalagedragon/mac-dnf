# adapted from homebrew's

%define major 68
%define minor 1

Name:           libicu4c
Version:        %{major}.%{minor}
Release:        1%{?dist}
Summary:        C/C++ libraries for Unicode and Globalization

License:        ICU
URL:            http://site.icu-project.org/home
%undefine       _disable_source_fetch
Source0:        https://github.com/unicode-org/icu/releases/download/release-%{major}-%{minor}/icu4c-%{major}_%{minor}-src.tgz
%define         SHA256SUM0 a9f2e3d8b4434b8e53878b4308bd1e6ee51c9c7042e2b1a376abefb6fbb29f2d

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
