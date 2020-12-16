%define system_python 3.9

Name:           libdnf
Version:        0.55.2
Release:        4%{?dist}
Summary:        This library provides a high level package-manager.

License:        LGPLv2+
URL:            https://github.com/rpm-software-management/libdnf
%undefine       _disable_source_fetch
Source0:        https://github.com/rpm-software-management/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 67e2113e5d27501163f96dd15e2fb76a4fcff9d861a5618e3a4d322e64cd5a28

Patch0:         libdnf-0001-limits-h.patch
Patch1:         libdnf-0002-error-types.patch
Patch2:         libdnf-0003-arch-detect.patch
Patch3:         libdnf-0004-usrlocal.patch
Patch4:         libdnf-0005-posixify-regex.patch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/rpm-software-management/libdnf.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+\\.\\d+)$" }

BuildRequires:  cmake swig gettext
BuildRequires:  pkg-config

BuildRequires: glib2-devel libsmartcols-devel
BuildRequires: libsolv-devel libcheck-devel librepo-devel
BuildRequires: libpython%{system_python}-devel libcppunit-devel
BuildRequires: libjson-c-devel
BuildRequires: libgpgme-devel
BuildRequires: libzchunk-devel
BuildRequires: python-sphinx
BuildRequires: libmodulemd-devel

Requires:      glib2
Requires:      libsmartcols
Requires:      libsolv
Requires:      librepo
Requires:      libpython%{system_python}
Requires:      libjson-c
Requires:      libgpgme
Requires:      libzchunk
Requires:      libmodulemd

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
%autosetup -n %{name}-%{version} -p0

sed -e '/SWIGWORDSIZE64/d' -I.orig bindings/python/CMakeLists.txt

%build

mkdir build
cd build

CFLAGS=-fno-lto CXXFLAGS=-fno-lto LDFLAGS=-fno-lto cmake -Wno-dev \
    -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python%{system_python} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPYTHON_DESIRED=3 \
    -DPYTHON_VERSION_MAJOR=3 -DWITH_MAN=0 -DWITH_GTKDOC=0 ..

%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# i don't even know
%{__install} -dm755 %{buildroot}%{_prefix}/lib/python%{system_python}/site-packages
mv %{buildroot}/{libdnf,hawkey} %{buildroot}%{_prefix}/lib/python%{system_python}/site-packages

mv %{buildroot}%{_prefix}/lib/python3.9/site-packages/hawkey/_hawkey.{dylib,so}

%files
%license COPYING
%{_prefix}/lib/libdnf.*.dylib
%{_prefix}/lib/libdnf
%{_prefix}/lib*/python%{system_python}/site-packages/hawkey
%{_prefix}/lib*/python%{system_python}/site-packages/libdnf
%{_datadir}/locale/*/LC_MESSAGES/libdnf.mo

%files devel
%{_includedir}/libdnf
%{_prefix}/lib/libdnf.dylib
%{_prefix}/lib/pkgconfig/*.pc

%changelog