%define system_python 3.9

%define libname gpgme

Name:           lib%{libname}
Version:        1.15.1
Release:        1%{?dist}
Summary:        GPGME is the standard library to access GnuPG functions from programming languages.

License:        LGPLv2+, GPLv2+
URL:            https://www.gnupg.org/
%undefine       _disable_source_fetch
Source0:        https://www.gnupg.org/ftp/gcrypt/%{libname}/%{libname}-%{version}.tar.bz2
%define         SHA256SUM0 eebc3c1b27f1c8979896ff361ba9bb4778b508b2496c2fc10e3775a40b1de1ad

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.gnupg.org/ftp/gcrypt/gpgme"}

BuildRequires:  gnupg
BuildRequires:  swig
BuildRequires:  libgpg-error-devel
BuildRequires:  libassuan-devel
BuildRequires:  pkg-config
BuildRequires:  libpython%{system_python}-devel

Requires:       libassuan libgpg-error

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libassuan-devel libgpg-error-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n gpgme
Summary:        Command-line utilities for libgpgme
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n gpgme

%package     -n python%{system_python}-%{name}
Summary:        Python %{system_python} bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}

%description -n python%{system_python}-%{name}

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version}
%build

mkdir build
cd build
%define _configure ../configure
export PYTHON_VERSION=%{system_python}
%configure --libdir=%{_prefix}/lib \
    --enable-languages=python

%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING COPYING.LESSER
%{_prefix}/lib/libgpgme.*.dylib
%exclude %{_prefix}/lib/python2.7
%doc %{_infodir}/*.info*

%files devel
%{_prefix}/bin/gpgme-config
%{_includedir}/*
%{_prefix}/lib/libgpgme.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%files -n gpgme
%{_prefix}/bin/gpgme-tool
%{_prefix}/bin/gpgme-json

%files -n python%{system_python}-%{name}
%{_prefix}/lib*/python%{system_python}/site-packages/gpg*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 1.15.1-1
  Updated to version 1.15.1.

* Sun Jan 10 2021 Morgan Thomas <m@m0rg.dev> 1.15.0-4
  Rebuilt with pythondistdeps generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.15.0-3
  Rebuilt with dependency generation.
