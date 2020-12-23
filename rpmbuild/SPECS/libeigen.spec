Name:           libeigen
Version:        3.3.9
Release:        1%{?dist}
Summary:        C++ template library for linear algebra

License:        MPL-2.0
URL:            https://eigen.tuxfamily.org/
%undefine       _disable_source_fetch
Source0:        https://gitlab.com/libeigen/eigen/-/archive/%{version}/eigen-%{version}.tar.gz
%define         SHA256SUM0 7985975b787340124786f092b3a07d594b2e9cd53bbfe5f3d9b1daee7d55f56f

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://gitlab.com/libeigen/eigen.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+\\.\\d+)$" }

BuildRequires:  cmake

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n eigen-%{version}

%build
mkdir build
cd build
cmake -Wno-dev \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%make_build

%install
cd build
%make_install

%{__install} -dm755 %{buildroot}%{_libdir}
mv -v %{buildroot}%{_datadir}/{eigen3/cmake,pkgconfig} %{buildroot}%{_libdir}/

%files
# libeigen is header-only

%files devel
%{_includedir}/eigen3
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*.pc

%changelog
