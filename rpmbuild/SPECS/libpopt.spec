%define libname popt

Name:           lib%{libname}
Version:        1.18
Release:        1%{?dist}
Summary:        This is the popt(3) command line option parsing library.

License:        MIT
URL:            https://github.com/rpm-software-management/popt/
%undefine       _disable_source_fetch
Source0:        http://ftp.rpm.org/%{libname}/releases/%{libname}-1.x/%{libname}-%{version}.tar.gz
%define         SHA256SUM0 5159bc03a20b28ce363aa96765f37df99ea4d8850b1ece17d1e6ad5c24fdc5d1

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/rpm-software-management/popt.git",
# X10-Update-Spec:   "pattern": "^popt-((?:\\d+\\.?)+)-release$" }

BuildRequires:  make
BuildRequires:  clang

%undefine _annotated_build
%global debug_package %{nil}

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
%configure --libdir=%{_prefix}/lib --disable-static
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang popt

%files -f build/popt.lang
%license COPYING
%{_prefix}/lib/libpopt.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libpopt.dylib
%{_prefix}/lib/pkgconfig/*.pc
%doc %{_mandir}/man3/*

%changelog

