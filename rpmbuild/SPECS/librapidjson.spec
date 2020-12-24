%define system_cmake 3.19

Name:           librapidjson
Version:        1.1.0
Release:        2%{?dist}
Summary:        A fast JSON parser/generator for C++ with SAX/DOM style API

License:        MIT
URL:            https://miloyip.github.io/rapidjson/
%undefine       _disable_source_fetch
Source0:        https://github.com/miloyip/rapidjson/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 bf7ced29704a1e696fbccf2a2b4ea068e7774fa37f6d7dd4039d0787f8bed98e

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/miloyip/rapidjson.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+\\.\\d+)$" }

BuildRequires:  doxygen
BuildRequires:  cmake%{system_cmake}

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n rapidjson-%{version}

# clang doesn't like it
sed -e 's/-march=native//' -i.orig CMakeLists.txt

%build

mkdir build
cd build

CXXFLAGS="$CXXFLAGS -Wno-zero-as-null-pointer-constant -Wno-shadow" cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..

%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
# rapidjson is header-only

%files devel
%{_includedir}/rapidjson
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/RapidJSON
%doc %{_docdir}/RapidJSON

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.1.0-2
  Rebuilt with dependency generation.
