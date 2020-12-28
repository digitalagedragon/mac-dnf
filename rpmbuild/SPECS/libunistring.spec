Name:           libunistring
Version:        0.9.10
Release:        1%{?dist}
Summary:        Library for manipulating Unicode strings

License:        GPLv3
URL:            https://gnu.org/software/libunistring
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/libunistring/libunistring-0.9.10.tar.xz
%define         SHA256SUM0 eb8fb2c3e4b6e2d336608377050892b54c3c983b646c561836550863003c05d7

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fv %{buildroot}%{_infodir}/dir

%files
%{_libdir}/libunistring.*.dylib

%files devel
%{_includedir}/*
%{_libdir}/libunistring.dylib
%{_docdir}/libunistring
%{_infodir}/*
%changelog
