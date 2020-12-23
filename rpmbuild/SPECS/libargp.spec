Name:           libargp
Version:        1.3
Release:        1%{?dist}
Summary:        Argument parsing functions from gnulib

License:        GPLv2+
URL:            https://www.lysator.liu.se/~nisse/misc/
%undefine       _disable_source_fetch
Source0:        https://www.lysator.liu.se/~nisse/misc/argp-standalone-%{version}.tar.gz
%define         SHA256SUM0 dec79694da1319acd2238ce95df57f3680fea2482096e483323fddf3d818d8be

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.lysator.liu.se/~nisse/misc/", "pattern": "argp-standalone-(\\d+(?:\\.\\d+)+)\\.tar\\.gz"}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n argp-standalone-%{version}
%build

%configure CFLAGS=-std=gnu89
%make_build

%install
%make_install

%{__install} -dm755 %{buildroot}%{_prefix}/lib
%{__install} -dm755 %{buildroot}%{_includedir}

%{__install} -m644 libargp.a %{buildroot}%{_prefix}/lib
%{__install} -m644 argp.h %{buildroot}%{_includedir}

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fv %{buildroot}%{_infodir}/dir

%files

%files devel
%{_includedir}/*
%{_prefix}/lib/libargp.a

%changelog
