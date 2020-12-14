%define major_version 2.67
%define patch_version 0

Name:           glib2
Version:        %{major_version}.%{patch_version}
Release:        1%{?dist}
Summary:        GLib library of C routines

License:        GPLv2+
URL:            http://www.gtk.org/
%undefine       _disable_source_fetch
Source0:        https://download.gnome.org/sources/glib/%{major_version}/glib-%{version}.tar.xz
%define         SHA256SUM0 0b15e57ab6c2bb90ced4e24a1b0d8d6e9a13af8a70266751aa3a45baffeed7c1

# X10-Update-Spec: { "type": "webscrape", "url": "https://download.gnome.org/sources/glib/cache.json"}

BuildRequires:  xz
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  libffi-devel
BuildRequires:  libpcre-devel

Requires:       libpcre
Requires:       libffi

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libffi-devel

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

mkdir build
meson -Dbuildtype=release --prefix=%{_prefix}  build/
ninja %{?_smp_mflags} -C build

%install
DESTDIR=%{buildroot} ninja -C build install

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
