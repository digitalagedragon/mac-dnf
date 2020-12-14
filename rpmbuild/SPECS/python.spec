%define pybasever 3.9
%define general_version %{pybasever}.1

Name:           python
Version:        %{general_version}
Release:        1%{?dist}
Summary:        The Python programming language

License:        Python-2.0
URL:            https://www.python.org/
%undefine       _disable_source_fetch
Source0:        https://www.python.org/ftp/python/%{version}/Python-%{version}.tgz
%define         SHA256SUM0 29cb91ba038346da0bd9ab84a0a55a845d872c341a4da6879f462e94c741f117

# no python updates until we figure out how we're doing python updates

BuildRequires:  libsqlite-devel

Requires:       libpython = %{version}-%{release}
Provides:       python%{pybasever} = %{version}-%{release}
Provides:       python(abi) = %{pybasever}

Requires:       libintl

# TODO is this stuff even kind of relevant on macOS
%undefine _annotated_build
%global debug_package %{nil}
# lib2to3 breaks all kinds of stuff on Fedora
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
# Turn off the brp-mangle-shebangs script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-mangle-shebangs[[:space:]].*$!!g')

%description

%package     -n libpython
Summary:        A library for embedding Python into other applications.
License:        Python-2.0
URL:            https://www.python.org/
Provides:       libpython%{pybasever} = %{version}-%{release}

%description -n libpython

%package     -n libpython-devel
Summary:        Development files for libpython
Requires:       libpython%{?_isa} = %{version}-%{release}
Requires:       python%{pybasever}
Provides:       libpython%{pybasever}-devel = %{version}-%{release}

%description -n libpython-devel
The libpython-devel package contains libraries and header files for
developing applications that use libpython.


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
ln -s python3 %{buildroot}/%{_bindir}/python

# cgi.py has a #! /usr/local/bin/python in it and it makes rpm (and therefore me) sad
rm %{buildroot}/%{_prefix}/lib/python%{pybasever}/cgi.py

%files
%license LICENSE
%{_bindir}/*
%doc %{_mandir}/man1/*
%{_prefix}/lib/python%{pybasever}

%files -n libpython
# TODO break this all out
%{_prefix}/lib/libpython%{pybasever}.dylib

%files -n libpython-devel
%{_includedir}/*
%{_prefix}/lib/pkgconfig/*.pc

%changelog
