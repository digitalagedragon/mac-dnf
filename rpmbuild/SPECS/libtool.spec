Name:           libtool
Version:        2.4.6
Release:        3%{?dist}
Summary:        Make building against shared libraries easier

License:        GPLv3+
URL:            https://gnu.org/software/libtool
%undefine       _disable_source_fetch
Source0:        https://ftpmirror.gnu.org/libtool/libtool-%{version}.tar.gz
%define         SHA256SUM0 e3bd4d5d3d025a36c21dd6af7ea818a2afcd4dfc1ea5a17b39d7854bcd0c06e3

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/libtool/"}

Provides:       glibtool = %{version}-%{release}

%description

%package     -n libltdl
Summary:        Cross-platform dynamic linking library
License:        LGPLv2

%description -n libltdl

%package     -n libltdl-devel
Summary:        Development files for libltdl
Requires:       libltdl%{?_isa} = %{version}-%{release}

%description -n libltdl-devel
The libltdl-devel package contains libraries and header files for
developing applications that use libltdl.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
./configure --bindir=%{_prefix}/opt/%{name}/bin --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%optlink

%optpost

%files
%license COPYING
%{_bindir}/*
%{_prefix}/opt/%{name}/bin
%{_datadir}/aclocal/*.m4
%{_datadir}/libtool
%doc %{_infodir}/*.info*
%doc %{_mandir}/man1/*

%files -n libltdl
%{_prefix}/lib/libltdl.*.dylib

%files -n libltdl-devel
%{_includedir}/*
%{_prefix}/lib/libltdl.dylib

%changelog

* Sun Dec 27 2020 Morgan Thomas <m@m0rg.dev> 2.4.6-3
  Install binaries under /usr/local/opt/libtool/bin.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 2.4.6-2
  Rebuilt with dependency generation.
