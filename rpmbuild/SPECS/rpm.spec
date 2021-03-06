%define system_python 3.9

Name:           rpm
Version:        4.16.1.2
Release:        13%{?dist}
Summary:        The RPM Package Manager (RPM) is a powerful package management system.

License:        GPLv2
URL:            https://rpm.org/
%undefine       _disable_source_fetch
Source0:        http://ftp.rpm.org/releases/rpm-4.16.x/rpm-%{version}.tar.bz2
%define         SHA256SUM0 8357329ceefc92c41687988b22198b26f74a12a9a68ac00728f934a5c4b4cacc

# X10-Update-Spec: { "type": "webscrape", "url": "http://rpm.org/timeline", "pattern": "RPM ((?:\\d+\\.?)+) released" }

Patch0:         rpm-0001-macos-arm64.patch
Patch1:         rpm-0002-lua-rawlen.patch
Patch2:         rpm-0003-bsd-sed.patch
Patch3:         rpm-0004-pkgconfig-path.patch
Patch4:         rpm-0005-python-paths.patch
Patch5:         rpm-0006-pythondist-paths.patch

Source1:        rpm-1000-macros.src
Source2:        rpm-1001-mach-fileattrs.src
Source3:        rpm-1002-machdeps.src
Source4:        rpm-1003-strip.src

BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python-%{system_python})
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  xz

Requires:       xz
Requires:       librpm = %{version}-%{release}
Requires:       libmagic
Requires:       libpopt
Requires:       libarchive
Requires:       libsqlite
Requires:       liblua
Requires:       libgcrypt
Requires:       pkg-config
Requires:       setuptools

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

%package     -n python%{system_python}-librpm
Summary:        Python %{system_python} bindings for %{name}
Requires:       librpm%{?_isa} = %{version}-%{release}
Provides:       python3-librpm

%description -n python%{system_python}-librpm

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
%{__install} -m644 -v %SOURCE2 %{buildroot}%{_prefix}/lib/rpm/fileattrs/mach.attr
%{__install} -m755 -v %SOURCE3 %{buildroot}%{_prefix}/lib/rpm/machdeps
%{__install} -m755 -v %SOURCE4 %{buildroot}%{_prefix}/lib/rpm/brp-strip
ln -svf brp-strip %{buildroot}%{_prefix}/lib/rpm/brp-strip-comment-note
ln -svf brp-strip %{buildroot}%{_prefix}/lib/rpm/brp-strip-shared
ln -svf brp-strip %{buildroot}%{_prefix}/lib/rpm/brp-strip-static-archive

echo '%%_prefix /usr/local' >>%{buildroot}%{_prefix}/lib/rpm/platform/%(uname -m | sed -e 's/arm64/aarch64/')-%(uname -s | tr '[:upper:]' '[:lower:]')/macros

sed -e "s|^/usr|%_prefix|" -Iold %{buildroot}%{_prefix}/lib/rpm/find-provides
sed -e "s|^/usr|%_prefix|" -Iold %{buildroot}%{_prefix}/lib/rpm/find-requires

## end random path fixes

# TODO... just TODO
rm %{buildroot}%{_prefix}/lib/rpm/fileattrs/perl*.attr

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

%files -n librpm-devel
%{_prefix}/lib/librpm.dylib
%{_prefix}/lib/librpmio.dylib
%{_prefix}/lib/librpmbuild.dylib
%{_prefix}/lib/librpmsign.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_includedir}/rpm

%files -n python%{system_python}-librpm
%{_prefix}/lib*/python%{system_python}/site-packages/rpm

%changelog

* Fri Jan 22 2021 Morgan Thomas <m@m0rg.dev> 4.16.1.2-13
  Remove obsolete libintl dependency.

* Sun Jan 10 2021 Morgan Thomas <m@m0rg.dev> 4.16.1.2-12
  Require setuptools as pythondistdeps depends on it.

* Sun Jan 10 2021 Morgan Thomas <m@m0rg.dev> 4.16.1.2-11
  Rebuilt with pythondistdeps generation.

* Sun Jan 10 2021 Morgan Thomas <m@m0rg.dev> 4.16.1.2-10
  Fix paths in fileattrs/python.attr.

* Sun Jan 10 2021 Morgan Thomas <m@m0rg.dev> 4.16.1.2-9
  Turn pythondistdeps.py back on.

* Mon Dec 28 2020 Morgan Thomas <m@m0rg.dev> 4.16.1.2-8
  Use pkgconfig dependencies.

* Sun Dec 27 2020 Morgan Thomas <m@m0rg.dev> 4.16.1.2-7
  Add /usr/local/opt management to macros.

* Sat Dec 26 2020 Morgan Thomas <m@m0rg.dev> 4.16.1.2-6
  Drop the set -x from brp-strip (whoops).

* Fri Dec 25 2020 Morgan Thomas <m@m0rg.dev> 4.16.1.2-5
  Adapt the brp-strip* scripts for macOS.

* Thu Dec 24 2020 Morgan Thomas <m@m0rg.dev> 4.16.1.2-4
  Use -mmacosx-version-min instead of -mmacos-version-min for compatibility.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 4.16.1.2-3
  Add pkg-config and Mach-O dependency generators.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 4.16.1.2-2
  Don't attempt to copy / merge directories in %umerge (how did that ever work?)

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 4.16.1.2-1
  Updated to version 4.16.1.2.

* Mon Dec 21 2020 Morgan Thomas <m@m0rg.dev> 4.16.1-15
  Add -mmacos-version-min to build flags and add basic CMake macros.

* Wed Dec 16 2020 Morgan Thomas <m@m0rg.dev> 4.16.1-14
  Explicitly disable zstd.

* Wed Dec 16 2020 Morgan Thomas <m@m0rg.dev> 4.16.1-13
  Explicitly pass __CURL.
