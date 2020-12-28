%define system_cmake 3.19

Name:           libsolv
Version:        0.7.16
Release:        5%{?dist}
Summary:        libsolv is a free package dependency solver using a satisfiability algorithm.

License:        BSD-3-Clause
URL:            https://github.com/openSUSE/libsolv
%undefine       _disable_source_fetch
Source0:        https://github.com/openSUSE/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 ed1753255792e9ae0582a1904c4baba5801036ef3efd559b65027e14ee1ea282

Patch0:         libsolv-0001-rpmdb-usrlocal.patch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/openSUSE/libsolv.git",
# X10-Update-Spec:   "pattern": "^((?:\\d+\\.?)+)$" }

BuildRequires:  cmake%{system_cmake}
BuildRequires:  pkgconfig(rpm)

%undefine _annotated_build
%global debug_package %{nil}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake%{system_cmake}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version} -p0

%build

mkdir build
cd build

cmake \
    -DENABLE_RPMMD=ON -DENABLE_RPMDB=ON -DENABLE_COMPLEX_DEPS=ON \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..

%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# can't get cmake to find this in the right place so we'll put it in
# the wrong place...
mv -v %{buildroot}%{_datadir}/cmake %{buildroot}%{_datadir}/cmake-%{system_cmake}

%files
%license LICENSE.BSD
%{_prefix}/bin/*
%{_prefix}/lib/libsolv.*.dylib
%{_prefix}/lib/libsolvext.*.dylib
%doc %{_mandir}/man1/*

%files devel
%{_includedir}/solv
%{_prefix}/lib/libsolv.dylib
%{_prefix}/lib/libsolvext.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_prefix}/share/cmake*/Modules/*.cmake

%doc %{_mandir}/man3/*

%changelog

* Mon Dec 28 2020 Morgan Thomas <m@m0rg.dev> 0.7.16-5
  Use pkgconfig dependencies.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 0.7.16-4
  Rebuilt with dependency generation.
