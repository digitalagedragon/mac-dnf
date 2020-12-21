%define system_python 3.9

Name:           rpm
Version:        4.16.1
Release:        15%{?dist}
Summary:        The RPM Package Manager (RPM) is a powerful package management system.

License:        GPLv2
URL:            https://rpm.org/
%undefine       _disable_source_fetch
Source0:        http://ftp.rpm.org/releases/rpm-4.16.x/rpm-%{version}.tar.bz2
%define         SHA256SUM0 4650cb9d414704059a6e0bee73a68a13bb367dfce188bd35f56b19e13a775cbf

# X10-Update-Spec: { "type": "webscrape", "url": "http://rpm.org/timeline", "pattern": "RPM ((?:\\d+\\.?)+) released" }

Patch0:         rpm-0001-macos-arm64.patch
Patch1:         rpm-0002-lua-rawlen.patch
Patch2:         rpm-0003-bsd-sed.patch

Source1:        rpm-1000-macros.src

BuildRequires:  libgcrypt-devel
BuildRequires:  libmagic-devel
BuildRequires:  libpopt-devel
BuildRequires:  libarchive-devel
BuildRequires:  libsqlite-devel
BuildRequires:  pkg-config
BuildRequires:  liblua-devel
BuildRequires:  libpython%{system_python}-devel
BuildRequires:  xz

Requires:       xz
Requires:       librpm = %{version}-%{release}
Requires:       libintl
Requires:       libmagic
Requires:       libpopt
Requires:       libarchive
Requires:       libsqlite
Requires:       liblua
Requires:       libgcrypt

%undefine _annotated_build

%description

%package     -n librpm
Summary:        A library for handling RPM packages.
License:        GPLv2
URL:            https://rpm.org/

%description -n librpm

%package     -n librpm-devel
Summary:        Development files for librpm
Requires:       librpm%{?_isa} = %{version}-%{release}
Requires:       libgcrypt-devel libpopt-devel libsqlite-devel
Requires:       libarchive-devel
Requires:       libpcre-devel
Requires:       libzstd-devel

%description -n librpm-devel
The librpm-devel package contains libraries and header files for
developing applications that use librpm.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -p0 -n rpm-%{version}
sed -e '1s/python/python3/' -Iold scripts/pythondistdeps.py

%build
export PYTHON=%{_prefix}/bin/python%{system_python}
export __CURL=/usr/bin/curl
%configure --libdir=%{_prefix}/lib --enable-bdb=no --enable-sqlite=yes --disable-openmp --enable-python \
    --enable-zstd=no \
    CFLAGS="-Wno-implicit-function-declaration -Wno-unused-function"
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -type f -exec sed -e 's|#!/usr/bin/python3|#!%{_prefix}/bin/python%{system_python}|' -i.sed_orig {} ';'
find %{buildroot} -name '*.sed_orig' -exec rm -f {} ';'

## begin random path fixes
# TODO should we have a /usr/local/bin/clang wrapper or something

%{__install} -m644 -v %SOURCE1 %{buildroot}%{_prefix}/lib/rpm/macros.d/macros.macrpm

echo '%%_prefix /usr/local' >>%{buildroot}%{_prefix}/lib/rpm/platform/%(uname -m | sed -e 's/arm64/aarch64/')-%(uname -s | tr '[:upper:]' '[:lower:]')/macros

sed -e "s|^/usr|%_prefix|" -Iold %{buildroot}%{_prefix}/lib/rpm/find-provides
sed -e "s|^/usr|%_prefix|" -Iold %{buildroot}%{_prefix}/lib/rpm/find-requires

## end random path fixes

# TODO... just TODO
rm %{buildroot}%{_prefix}/lib/rpm/fileattrs/perl*.attr
rm %{buildroot}%{_prefix}/lib/rpm/fileattrs/python*.attr

%find_lang rpm

%files -f rpm.lang
%license COPYING
# TODO split rpmbuild out
%{_bindir}/*
%doc %{_mandir}/man{1,8}/*
%doc %{_mandir}/*/man{1,8}/*

%files -n librpm
%{_prefix}/lib/librpm.*.dylib
%{_prefix}/lib/librpmio.*.dylib
%{_prefix}/lib/librpmbuild.*.dylib
%{_prefix}/lib/librpmsign.*.dylib
%{_prefix}/lib/rpm-plugins
%{_prefix}/lib/rpm
%{_prefix}/lib*/python%{system_python}/site-packages/rpm

%files -n librpm-devel
%{_prefix}/lib/librpm.dylib
%{_prefix}/lib/librpmio.dylib
%{_prefix}/lib/librpmbuild.dylib
%{_prefix}/lib/librpmsign.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_includedir}/rpm

%changelog

* Mon Dec 21 2020 Morgan Thomas <m@m0rg.dev> 4.16.1 release 15
  Add -mmacos-version-min to build flags and add basic CMake macros.

* Wed Dec 16 2020 Morgan Thomas <m@m0rg.dev> 4.16.1 release 14
  Explicitly disable zstd.

* Wed Dec 16 2020 Morgan Thomas <m@m0rg.dev> 4.16.1 release 13
  Explicitly pass __CURL.
