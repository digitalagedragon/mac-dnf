%define major_version 2.67
%define patch_version 2
%enable_universal

Name:           %{universal glib2}
Version:        %{major_version}.%{patch_version}
Release:        1%{?dist}
Summary:        GLib library of C routines

License:        GPLv2+
URL:            http://www.gtk.org/
%undefine       _disable_source_fetch
Source0:        https://download.gnome.org/sources/glib/%{major_version}/glib-%{version}.tar.xz
%define         SHA256SUM0 b41d42d6c572e1e420ffc38a077e0157e0b53b5a94c9647a3dc3701043c3b69b

# X10-Update-Spec: { "type": "webscrape", "url": "https://download.gnome.org/sources/glib/cache.json"}

%uprovides      glib2

BuildRequires:  xz
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  %{universal libffi}-devel
BuildRequires:  %{universal libpcre}-devel
BuildRequires:  pkg-config

Requires:       %{universal libpcre}
Requires:       %{universal libffi}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{universal libffi}-devel
Requires:       %{universal libpcre}-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        utils
Summary:        Command-line utilites for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n glib-%{version}

%build

%ufor -n
mkdir %{uarchdir build}
meson -Dbuildtype=release --prefix=%{_prefix} %{uarchdir build}
ninja %{?_smp_mflags} -C %{uarchdir build} --verbose
%udone

%install
%uinstall -n DESTDIR=%{ubuildroot} ninja -C %{uarchdir build} install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang glib20

%files -f glib20.lang
%license COPYING
%{_prefix}/lib/libgio-2.0.*.dylib
%{_prefix}/lib/libglib-2.0.*.dylib
%{_prefix}/lib/libgmodule-2.0.*.dylib
%{_prefix}/lib/libgobject-2.0.*.dylib
%{_prefix}/lib/libgthread-2.0.*.dylib

%files devel
%{_includedir}/*
%{_prefix}/lib/libgio-2.0.dylib
%{_prefix}/lib/libglib-2.0.dylib
%{_prefix}/lib/libgmodule-2.0.dylib
%{_prefix}/lib/libgobject-2.0.dylib
%{_prefix}/lib/libgthread-2.0.dylib
%{_datadir}/gdb/auto-load/%{_prefix}/lib/*.py
%{_prefix}/lib/glib-2.0
%{_prefix}/lib/pkgconfig/*.pc
%{_datadir}/glib-2.0
%{_datadir}/aclocal/*.m4
%{_datadir}/gettext/its/gschema.*

%files utils
%{_bindir}/gdbus
%{_bindir}/gdbus-codegen
%{_bindir}/gio
%{_bindir}/gio-querymodules
%{_bindir}/glib-compile-resources
%{_bindir}/glib-compile-schemas
%{_bindir}/glib-genmarshal
%{_bindir}/glib-gettextize
%{_bindir}/glib-mkenums
%{_bindir}/gobject-query
%{_bindir}/gresource
%{_bindir}/gsettings
%{_bindir}/gtester
%{_bindir}/gtester-report
%{_datadir}/bash-completion/completions/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 2.67.2-1
  Updated to version 2.67.2.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 2.67.1-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 2.67.1-1
  Updated to version 2.67.1.
