Name:           swig
Version:        4.0.2
Release:        3%{?dist}
Summary:        Multi-language bindings generator

License:        GPLv3+, MIT
URL:            http://www.swig.org/
%undefine       _disable_source_fetch
Source0:        https://github.com/swig/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 b5f43d5f94c57ede694ffe5e805acc5a3a412387d7f97dcf290d06c46335cb0b

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/swig/swig.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(libpcre)

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup
./autogen.sh

%build
# swig is one of those silly things that will absolutely bring weird CFLAGS along
# from the build machine
./configure --prefix=%{_prefix} 
%make_build

%install
%make_install

%files
%license COPYRIGHT LICENSE LICENSE-GPL LICENSE-UNIVERSITIES
%{_bindir}/*
%{_datadir}/swig

%changelog

* Mon Dec 28 2020 Morgan Thomas <m@m0rg.dev> 4.0.2-3
  Use pkgconfig dependencies.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 4.0.2-2
  Rebuilt with dependency generation.
