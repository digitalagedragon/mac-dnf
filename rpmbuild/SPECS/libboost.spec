%define system_python 3.9

Name:           libboost
Version:        1.75.0
Release:        2%{?dist}
Summary:        A collection of C++ libraries

License:        BSL-1.0
URL:            https://www.boost.org
%undefine       _disable_source_fetch
Source0:        https://dl.bintray.com/boostorg/release/%{version}/source/boost_%(echo %{version} | tr . _).tar.bz2
%define         SHA256SUM0 953db31e016db7bb207f11432bef7df100516eeb746843fa0486a222e3fd49cb

# X10-Update-Spec: { "type": "webscrape", "url": "https://www.boost.org/feed/downloads.rss", "pattern": ">Version v?(\\d+(?:\\.\\d+)+)<"}

BuildRequires:  libicu4c-devel
BuildRequires:  libzstd-devel
BuildRequires:  liblzma-devel
BuildRequires:  libpython%{system_python}-devel

Requires:       libicu4c
Requires:       libzstd
Requires:       liblzma
Requires:       libpython%{system_python}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n boost_%(echo %{version} | tr . _)

%build

./bootstrap.sh --prefix=%{_prefix} --without-libraries=mpi
./b2 headers
./b2 --prefix=%{_prefix} -d2 %{?_smp_mflags} \
    --layout=tagged-1.66 \
    threading=multi,single \
    link=shared \
    python=%{system_python}

%install
./b2 --prefix=%{buildroot}%{_prefix} -d2 %{?_smp_mflags} \
    --layout=tagged-1.66 \
    install \
    threading=multi,single \
    link=shared \
    python=%{system_python}

%files
%{_libdir}/*.dylib

%files devel
%{_includedir}/boost
%{_libdir}/cmake/*
%{_libdir}/*.a

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.75.0-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.75.0-1
  Updated to version 1.75.0.

