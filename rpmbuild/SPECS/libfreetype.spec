Name:           libfreetype
Version:        2.10.4
Release:        1%{?dist}
Summary:        A freely available software library to render fonts

License:        FTL
URL:            https://freetype.org
%undefine       _disable_source_fetch
Source0:        https://downloads.sourceforge.net/project/freetype/freetype2/%{version}/freetype-%{version}.tar.xz
%define         SHA256SUM0 86a854d8905b19698bbc8f23b860bc104246ce4854dcea8e3b0fb21284f75784

BuildRequires:  xz

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n freetype-%{version}

%build

mkdir build
cd build
%define _configure ../configure
%configure --disable-static --enable-freetype-config --without-harfbuzz
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license docs/LICENSE.TXT
%{_libdir}/libfreetype.*.dylib

%files devel
%{_bindir}/freetype-config
%{_includedir}/*
%{_libdir}/libfreetype.dylib
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%doc %{_mandir}/man1/*

%changelog
