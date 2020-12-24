%define system_python 3.9

%define libname librepo

Name:           %{libname}
Version:        1.12.1
Release:        6%{?dist}
Summary:        A library providing C and Python (libcURL like) API for downloading linux repository metadata and packages

License:        LGPLv2
URL:            http://rpm-software-management.github.io/librepo/
%undefine       _disable_source_fetch
Source0:        https://github.com/rpm-software-management/%{libname}/archive/%{version}.tar.gz#/%{libname}-%{version}.tar.gz
%define         SHA256SUM0 b78113f3aeb0d562b034dbeb926609019b7bed27e05c9ab5a584a9938de8da9f

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/rpm-software-management/librepo.git",
# X10-Update-Spec:   "pattern": "^((?:\\d+\\.?)+)$" }

BuildRequires: cmake
BuildRequires: pkg-config
BuildRequires: libzchunk-devel
BuildRequires: glib2-devel libopenssl-devel
BuildRequires: libcurl-devel libpython%{system_python}-devel
BuildRequires: libcheck-devel libgpgme-devel
BuildRequires: libxml2-devel

Requires: glib2 libopenssl libcurl libpython
Requires: libgpgme
Requires: libzchunk
Requires: libxml2

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel libopenssl-devel
Requires:       libxml2-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{libname}-%{version}

%build

mkdir build
cd build
%set_build_flags
CFLAGS="-D_DARWIN_C_SOURCE -L%{_prefix}/lib" cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DPYTHON_DESIRED=3 -DPYTHON_EXECUTABLE:FILEPATH=%{_prefix}/bin/python%{system_python} \
    -DENABLE_TESTS=0 ..
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%{_prefix}/lib/librepo.*.dylib
%{_prefix}/lib*/python%{system_python}/site-packages/librepo

%files devel
%{_prefix}/include/librepo
%{_prefix}/lib/librepo.dylib
%{_prefix}/lib/pkgconfig/*.pc

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.12.1-6
  Rebuilt with dependency generation.

* Wed Dec 16 2020 Morgan Thomas <m@m0rg.dev> 1.12.1 release 5
  Add libzchunk to build dependencies.