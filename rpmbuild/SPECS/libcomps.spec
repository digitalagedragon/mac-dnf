%define system_python 3.9

Name:           libcomps
Version:        0.1.15
Release:        3%{?dist}
Summary:        Libcomps is alternative for yum.comps library

License:        GPLv2
URL:            https://github.com/rpm-software-management/libcomps
%undefine       _disable_source_fetch
Source0:        https://github.com/rpm-software-management/libcomps/archive/%{name}-%{version}.tar.gz
%define         SHA256SUM0 3304bf7b178fd719fff6fe67f365b63e486f2f5e3e6e0ff1780f42723776cb61

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/rpm-software-management/libcomps.git",
# X10-Update-Spec:   "pattern": "^libcomps-(\\d+\\.\\d+(?:\\.\\d+)?)$" }

BuildRequires:  cmake

BuildRequires: libxml2-devel
BuildRequires: libcheck-devel
BuildRequires: libpython%{system_python}-devel

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n python%{system_python}-%{name}
Summary:        Python %{system_python} bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}

%description -n python%{system_python}-%{name}

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{name}-%{version}

%build

mkdir build
cd build

cmake -Wno-dev -DENABLE_TESTS=0 \
    -DPYTHON_EXECUTABLE:FILEPATH=/usr/local/bin/python%{system_python} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPYTHON_DESIRED=3 ../libcomps

%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
mv %{buildroot}%{_prefix}/lib/python3.9/site-packages/libcomps/_libpycomps.{dylib,so}

%files
%license COPYING
%{_prefix}/lib/libcomps.*.dylib

%files devel
%{_includedir}/libcomps
%{_prefix}/lib/libcomps.dylib
%{_prefix}/lib/pkgconfig/*.pc

%files -n python%{system_python}-%{name}
%{_prefix}/lib*/python%{system_python}/site-packages/libcomps*

%changelog

* Sun Jan 10 2021 Morgan Thomas <m@m0rg.dev> 0.1.15-3
  Rebuilt with pythondistdeps generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 0.1.15-2
  Rebuilt with dependency generation.
