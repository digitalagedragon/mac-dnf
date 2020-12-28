%define pybasever 3.9
%define general_version %{pybasever}.1

%define is_system_python 1

Name:           python%{pybasever}
Version:        %{general_version}
Release:        7%{?dist}
Summary:        The Python programming language

License:        Python-2.0
URL:            https://www.python.org/
%undefine       _disable_source_fetch
Source0:        https://www.python.org/ftp/python/%{version}/Python-%{version}.tgz
%define         SHA256SUM0 29cb91ba038346da0bd9ab84a0a55a845d872c341a4da6879f462e94c741f117

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.python.org/ftp/python/", "pattern": "\"(3\\.9\\.\\d+)/\""}

BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libssl)

# the unversioned ones don't exist anymore
# TODO remove this in 3.10 because it was a bad idea
Obsoletes:      python <= 3.9.1-1
Obsoletes:      libpython <= 3.9.1-1
Obsoletes:      libpython-devel <= 3.9.1-1

Requires:       libpython%{pybasever} = %{version}-%{release}

Requires:       libintl
Requires:       libsqlite
Requires:       libopenssl

# lib2to3 breaks all kinds of stuff on Fedora
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
# Turn off the brp-mangle-shebangs script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-mangle-shebangs[[:space:]].*$!!g')

%description

%package     -n lib%{name}
Summary:        A library for embedding Python into other applications.
License:        Python-2.0
URL:            https://www.python.org/

%description -n lib%{name}

%package     -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
The lib%{name}-devel package contains libraries and header files for
developing applications that use lib%{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n Python-%{version}

%build

./configure --prefix=%{_prefix} --libdir=%{_prefix}/lib \
    --disable-ipv6 --without-ensurepip \
    --enable-shared \
    ac_cv_file__dev_ptmx=yes \
    ac_cv_file__dev_ptc=no
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%if %{is_system_python}
ln -s python3 %{buildroot}/%{_bindir}/python
%else
rm -fv %{buildroot}/%{_bindir}/python3
rm -fv %{buildroot}/%{_bindir}/python3-config
rm -fv %{buildroot}/%{_bindir}/pydoc3
rm -fv %{buildroot}/%{_bindir}/idle3
rm -fv %{buildroot}/%{_bindir}/2to3
rm -fv %{buildroot}/%{_libdir}/pkgconfig/python3.pc
rm -fv %{buildroot}/%{_libdir}/pkgconfig/python3-embed.pc
rm -fv %{buildroot}/%{_mandir}/man1/python3.1*
%endif

%files
%license LICENSE
%{_bindir}/*
%doc %{_mandir}/man1/*
%{_prefix}/lib/python%{pybasever}

%files -n lib%{name}
# TODO break this all out
%{_prefix}/lib/libpython%{pybasever}.dylib

%files -n lib%{name}-devel
%{_includedir}/*
%{_prefix}/lib/pkgconfig/*.pc

%changelog

* Mon Dec 28 2020 Morgan Thomas <m@m0rg.dev> 3.9.1-7
  Use pkgconfig dependencies.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.9.1-5
  Rebuilt with dependency generation.

* Thu Dec 17 2020 Morgan Thomas <m@m0rg.dev> 3.9.1-4
  Build with SSL support.

* Thu Dec 17 2020 Morgan Thomas <m@m0rg.dev> 3.9.1-3
  Stop not packaging cgi.py.

* Wed Dec 16 2020 Morgan Thomas <m@m0rg.dev> 3.9.1-2
  Infrastructure for multiple python versions.
