Name:           libflame
Version:        5.2.0
Release:        1%{?dist}
Summary:        A portable library for dense matrix computations

License:        BSD-3-Clause
URL:            https://www.cs.utexas.edu/~flame/web/libFLAME.html
%undefine       _disable_source_fetch
Source0:        https://github.com/flame/libflame/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 997c860f351a5c7aaed8deec00f502167599288fd0559c92d5bfd77d0b4d475c

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
%configure --enable-lapack2flame
%make_build

%install
%make_install

%files

%files devel

%changelog
