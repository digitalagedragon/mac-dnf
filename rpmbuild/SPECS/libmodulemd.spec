%define system_python 3.9

Name:           libmodulemd
Version:        2.11.1
Release:        2%{?dist}
Summary:        C Library for manipulating module metadata files

License:        MIT
URL:            https://github.com/fedora-modularity/libmodulemd
%undefine       _disable_source_fetch
Source0:        https://github.com/fedora-modularity/libmodulemd/releases/download/%{name}-%{version}/modulemd-%{version}.tar.xz
%define         SHA256SUM0 bbb9ca09fe1a732277386afb9f96d150dc1e62c72bc3c0e556ce605c36b7f769

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/fedora-modularity/libmodulemd.git",
# X10-Update-Spec:   "pattern": "^libmodulemd-((?:\\d+\\.?)+)$" }

BuildRequires:  meson ninja-build

BuildRequires: pkg-config
BuildRequires: glib2-devel libyaml-devel
BuildRequires: librpm-devel libmagic-devel
BuildRequires: python%{system_python}
BuildRequires: glib2-utils

Requires:      glib2
Requires:      libyaml
Requires:      librpm
Requires:      libmagic

%undefine _annotated_build
%global debug_package %{nil}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       librpm-devel libyaml-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -p1 -n modulemd-%{version}

%build

mkdir build

meson -Dbuildtype=release -Dnative=true \
    -Dwith_docs=false -Ddeveloper_build=false -Dskip_introspection=true -Dwith_manpages=disabled \
    -Dgobject_overrides_dir_py3='/usr/lib/python%{system_python}/site-packages/gi/overrides' \
    --prefix=%{_prefix} \
    build/
ninja %{?_smp_mflags} -C build

%install
DESTDIR=%{buildroot} ninja -C build install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%{_prefix}/lib/libmodulemd.*.dylib
%exclude /usr/lib/python%{system_python}/site-packages/gi/overrides/*

%files devel
%{_includedir}/*
%{_prefix}/lib/pkgconfig/*.pc
%{_prefix}/lib/libmodulemd.dylib
# TODO
# %doc %%{_datadir}/gtk-doc/html/modulemd-2.0

%{_bindir}/modulemd-validator

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 2.11.1-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 2.11.1-1
  Updated to version 2.11.1.

* Wed Dec 16 2020 Morgan Thomas <m@m0rg.dev> 2.10.0 release 2
  Add pkg-config and glib2-utils to buildrequires.
