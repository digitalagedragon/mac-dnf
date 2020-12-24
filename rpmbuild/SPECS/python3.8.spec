%define pybasever 3.8
%define general_version %{pybasever}.7

%define is_system_python 0

%if %{is_system_python}
Name:           python
%else
Name:           python%{pybasever}
%endif
Version:        %{general_version}
Release:        2%{?dist}
Summary:        The Python programming language

License:        Python-2.0
URL:            https://www.python.org/
%undefine       _disable_source_fetch
Source0:        https://www.python.org/ftp/python/%{version}/Python-%{version}.tgz
%define         SHA256SUM0 20e5a04262f0af2eb9c19240d7ec368f385788bba2d8dfba7e74b20bab4d2bac

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.python.org/ftp/python/", "pattern": "\"(3\\.8\\.\\d+)/\""}

Patch0:         python3.8-0001-macos-arm64.patch

BuildRequires:  libsqlite-devel

Requires:       libpython%{pybasever} = %{version}-%{release}
%if %{is_system_python}
Provides:       python = %{version}-%{release}
%endif
Provides:       python(abi) = %{pybasever}

Requires:       libintl

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
%if %{is_system_python}
Provides:       libpython = %{version}-%{release}
%endif

%description -n lib%{name}

%package     -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{is_system_python}
Provides:       libpython-devel = %{version}-%{release}
%endif

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

# cgi.py has a #! /usr/local/bin/python in it and it makes rpm (and therefore me) sad
rm %{buildroot}/%{_prefix}/lib/python%{pybasever}/cgi.py

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

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.8.7-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.8.7-1
  Updated to version 3.8.7.
