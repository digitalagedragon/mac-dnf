Name:           lua
Version:        5.4.2
Release:        3%{?dist}
Summary:        Lua is a powerful, efficient, lightweight, embeddable scripting language.

License:        MIT
URL:            https:///www.lua.org
%undefine       _disable_source_fetch
Source0:        https://www.lua.org/ftp/%{name}-%{version}.tar.gz
%define         SHA256SUM0 11570d97e9d7303c0a59567ed1ac7c648340cd0db10d5fd594c09223ef2f524f

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.lua.org/ftp/", "pattern": "(?:HREF=\"|/)\\w+-((?:\\d+\\.)*\\d+)\\.tar\\..z2?\""}

Patch0:         liblua-0001-dynamic-library.patch

%undefine _annotated_build
%define   debug_package %{nil}

%description

%package     -n liblua
Summary:        lua(1), but library (empty package for consistency with shared libraries)
License:        MIT
URL:            https:///www.lua.org

%description -n liblua

%package     -n liblua-devel
Summary:        Development files for liblua
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n liblua-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version} -p0

%build
export CFLAGS=""
export LDFLAGS=""
# lua is too cool for autoconf
make %{_smp_mflags} CC="%{?target_tool_prefix}gcc -std=gnu99" AR="%{?target_tool_prefix}ar rcu" RANLIB="%{?target_tool_prefix}ranlib" MYCFLAGS="-fPIC" MYLDFLAGS="-fPIC"

%install
%make_install INSTALL_TOP=%{buildroot}/%{_prefix} INSTALL_MAN=%{buildroot}/%{_mandir}/man1
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# lua is also too cool for pkgconfig
install -dm755 %{buildroot}/%{_prefix}/lib/pkgconfig
cat > %{buildroot}/%{_prefix}/lib/pkgconfig/lua.pc << "EOF"
R=%{version}
V=${R%.*}

prefix=%{_prefix}
INSTALL_BIN=${prefix}/bin
INSTALL_INC=${prefix}/include
INSTALL_LIB=${prefix}/lib
INSTALL_MAN=${prefix}/share/man/man1
INSTALL_LMOD=${prefix}/share/lua/${V}
INSTALL_CMOD=${prefix}/lib/lua/${V}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: Lua
Description: An Extensible Extension Language
Version: ${R}
Requires:
Libs: -L${libdir} -llua -lm -ldl
Cflags: -I${includedir}
EOF

%files
%license doc/readme.html
%{_bindir}/*
%doc %{_mandir}/man1/*

%files -n liblua
%{_prefix}/lib/liblua.*.dylib

%files -n liblua-devel
%{_prefix}/lib/pkgconfig/lua.pc
%{_includedir}/*
%{_prefix}/lib/liblua.dylib

%changelog

* Fri Jan 01 2021 Morgan Thomas <m@m0rg.dev> 5.4.2-3
  Clean up redundant dependencies.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 5.4.2-2
  Rebuilt with dependency generation.
