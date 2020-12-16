%define system_python 3.9

Name:           libxml2
Version:        2.9.10
Release:        4%{?dist}
Summary:        Libxml2 is the XML C parser and toolkit developed for the Gnome project

License:        MIT
URL:            http://xmlsoft.org/
%undefine       _disable_source_fetch
Source0:        ftp://xmlsoft.org/%{name}/%{name}-%{version}.tar.gz
%define         SHA256SUM0 aafee193ffb8fe0c82d4afef6ef91972cbaf5feea100edc2f262750611b4be1f

# upstream commit e4fb36841800038c289997432ca547c9bfef9db1, not yet released
Patch0:         libxml2-0001-python-parentheses.patch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://gitlab.gnome.org/GNOME/libxml2.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

BuildRequires: libpython%{system_python}-devel
BuildRequires: pkg-config
BuildRequires: liblzma-devel

Requires:      liblzma

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       liblzma-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version} -p 0

%package        utils
Summary:        Command-line utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils

%build

mkdir build
cd build
%define _configure ../configure
%configure --libdir=%{_prefix}/lib
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%{_prefix}/lib/libxml2.*.dylib
%{_prefix}/lib/python%{system_python}/site-packages/*
%doc %{_datadir}/doc/libxml2-python-%{version}
%doc %{_datadir}/gtk-doc/html/libxml2
%doc %{_datadir}/doc/libxml2-%{version}

%files devel
%{_includedir}/libxml2
%{_prefix}/lib/libxml2.dylib
%{_prefix}/lib/*.a
# was this supposed to go in libexec or something?
%{_prefix}/lib/xml2Conf.sh
%{_prefix}/lib/pkgconfig/*.pc
%{_prefix}/lib/cmake/libxml2
%{_datadir}/aclocal/*.m4
%doc %{_mandir}/man3/*

%files utils
%{_bindir}/xml2-config
%{_bindir}/xmlcatalog
%{_bindir}/xmllint
%doc %{_mandir}/man1/*

%changelog

* Wed Dec 16 2020 Morgan Thomas <m@m0rg.dev> 2.9.10 release 4
  Add liblzma-devel/liblzma to requires
