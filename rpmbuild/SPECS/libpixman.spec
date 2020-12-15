%enable_universal

Name:           %{universal libpixman}
Version:        0.40.0
Release:        2%{?dist}
Summary:        cairo's pixel manipulation library

License:        LGPLv2
URL:            https://cairographics.org/
%undefine       _disable_source_fetch
Source0:        https://cairographics.org/releases/pixman-0.40.0.tar.gz
%define         SHA256SUM0 6d200dec3740d9ec4ec8d1180e25779c00bc749f94278c8b9021f5534db223fc

%uprovides libpixman

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%uprovides libpixman devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n pixman-%{version} -p0

%build

%ufor
%configure --disable-static
%make_build
%udone

%install
%uinstall

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%{_libdir}/libpixman-1.*.dylib

%files devel
%{_includedir}/pixman-1
%{_libdir}/libpixman-1.dylib
%{_libdir}/pkgconfig/*.pc

%changelog
