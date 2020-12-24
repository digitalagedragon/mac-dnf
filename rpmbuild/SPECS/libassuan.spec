Name:           libassuan
Version:        2.5.4
Release:        2%{?dist}
Summary:        Libassuan is a small library implementing the so-called Assuan protocol.

License:        LGPLv2+
URL:            https://www.gnupg.org/
%undefine       _disable_source_fetch
Source0:        https://www.gnupg.org/ftp/gcrypt/%{name}/%{name}-%{version}.tar.bz2
%define         SHA256SUM0 c080ee96b3bd519edd696cfcebdecf19a3952189178db9887be713ccbcb5fbf0

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.gnupg.org/ftp/gcrypt/libassuan/"}

BuildRequires:  libgpg-error-devel
BuildRequires:  pkg-config

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version}

%build

mkdir build
cd build
%define _configure ../configure
%configure --libdir=%{_prefix}/lib
%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%files
%license COPYING.LIB
%{_prefix}/lib/libassuan.*.dylib
%doc %{_infodir}/*.info*

%files devel
%{_prefix}/bin/libassuan-config
%{_includedir}/*
%{_prefix}/lib/libassuan.dylib
%{_prefix}/lib/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 2.5.4-2
  Rebuilt with dependency generation.
