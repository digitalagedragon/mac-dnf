%define system_python 3.9

Name:           createrepo_c
Version:        0.16.2
Release:        2%{?dist}
Summary:        Tool for building yum repos

License:        GPLv2
URL:            https://github.com/rpm-software-management/createrepo_c
%undefine       _disable_source_fetch
Source0:        https://github.com/rpm-software-management/createrepo_c/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 cbb9650e0e61895284c398dfa1480f0a4907881e467f968fafdba3b06d1c56fa

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/rpm-software-management/createrepo_c.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+\\.\\d+)$" }

BuildRequires:  libmagic-devel
BuildRequires:  glib2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmodulemd-devel
BuildRequires:  libxml2-devel
BuildRequires:  libpython%{system_python}-devel
BuildRequires:  librpm-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libsqlite-devel
BuildRequires:  libzchunk-devel
BuildRequires:  pkg-config

BuildRequires:  cmake

Requires:       libcreaterepo_c

%undefine _annotated_build

%description

%package     -n libcreaterepo_c
Summary:        Library interface to createrepo_c

%description -n libcreaterepo_c

%package     -n libcreaterepo_c-devel
Summary:        Development files for libcreaterepo_c
Requires:       libcreaterepo_c%{?_isa} = %{version}-%{release}

%description -n libcreaterepo_c-devel
The libcreaterepo_c-devel package contains libraries and header files for
developing applications that use libcreaterepo_c.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

sed -e '/unset(PYTHON_EXECUTABLE/d' -i.orig src/python/CMakeLists.txt

%build
mkdir build
cd build
%set_build_flags
CFLAGS="-Wno-implicit-function-declaration" cmake -Wno-dev \
    -DPYTHON_DESIRED=3 \
    -DPYTHON_EXECUTABLE:FILEPATH=/usr/local/bin/python%{system_python} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} -DENABLE_DRPM=OFF -DWITH_LIBMODULEMD=OFF ..

%make_build

%install
cd build
%make_install

%files
%license COPYING
%{_bindir}/*
%{_prefix}/lib*/python%{system_python}/site-packages/*
%doc %{_mandir}/man8/*

%files -n libcreaterepo_c
%{_prefix}/lib/libcreaterepo_c.*.dylib

%files -n libcreaterepo_c-devel
%{_prefix}/lib/libcreaterepo_c.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_includedir}/*

%changelog
