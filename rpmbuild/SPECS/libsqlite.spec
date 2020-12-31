%define libname sqlite
%define real_version %(echo %{version} | perl -nE '@v=split /\\./;$v[3]//=0;print shift@v;say map{sprintf("%02d",$_)}@v;')

Name:           lib%{libname}
Version:        3.34.0
Release:        3%{?dist}
Summary:        SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

License:        Public domain
URL:            https://sqlite.org
%undefine       _disable_source_fetch
Source0:        https://sqlite.org/2020/sqlite-autoconf-%{real_version}.tar.gz
%define         SHA256SUM0 bf6db7fae37d51754737747aaaf413b4d6b3b5fbacd52bdb2d0d6e5b2edd9aee

# X10-Update-Spec: { "type": "webscrape",
# X10-Update-Spec:   "url": "https://sqlite.org/index.html",
# X10-Update-Spec:   "pattern": "Version ((?:\\d+\\.?)+)" }

%undefine _annotated_build
%global debug_package %{nil}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     sqlite
Summary:        sqlite command line interface

%description -n sqlite

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n sqlite-autoconf-%{real_version}

%build

mkdir build
cd build
export CFLAGS="-g -O2 -DSQLITE_ENABLE_FTS3=1 \
    -DSQLITE_ENABLE_FTS4=1 -DSQLITE_ENABLE_COLUMN_METADATA=1 \
    -DSQLITE_ENABLE_UNLOCK_NOTIFY=1 -DSQLITE_ENABLE_DBSTAT_VTAB=1 \
    -DSQLITE_SECURE_DELETE=1 -DSQLITE_ENABLE_FTS3_TOKENIZER=1"
export LDFLAGS=""
../configure --prefix=%{_prefix} --bindir=%{_prefix}/opt/%{name}/bin \
    --enable-fts5  --disable-static
%make_build

%posttrans -n sqlite
echo Note: macOS provides its own sqlite3, so %{name}\\'s binaries have been installed under /usr/local/opt/%{name}/bin.

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%{_prefix}/lib/libsqlite3.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libsqlite3.dylib
%{_prefix}/lib/pkgconfig/*.pc

%files -n sqlite
%{_prefix}/opt/%{name}/bin/sqlite3
%doc %{_mandir}/man1/*

%changelog

* Thu Dec 31 2020 Morgan Thomas <m@m0rg.dev> 3.34.0-3
  Move sqlite3 to /usr/local/opt.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.34.0-2
  Rebuilt with dependency generation.
