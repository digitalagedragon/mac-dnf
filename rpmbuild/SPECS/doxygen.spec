%define system_cmake 3.19

Name:           doxygen
Version:        1.9.1
Release:        1%{?dist}
Summary:        Documentation generator

License:        GPLv2
URL:            https://www.doxygen.org
%undefine       _disable_source_fetch
Source0:        https://doxygen.nl/files/doxygen-%{version}.src.tar.gz
%define         SHA256SUM0 67aeae1be4e1565519898f46f1f7092f1973cce8a767e93101ee0111717091d1

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/doxygen/doxygen",
# X10-Update-Spec:   "pattern": "^Release_(\\d+_\\d+_\\d+)$" }

BuildRequires:  cmake%{system_cmake}
BuildRequires:  bison

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build

mkdir build
cd build

cmake \
    -DBISON_EXECUTABLE=%(which gbison) \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..

%make_build

%install
cd build
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license LICENSE
%{_bindir}/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 1.9.1-1
  Updated to version 1.9.1.

* Sun Dec 27 2020 Morgan Thomas <m@m0rg.dev> 1.9.0-1
  Updated to version 1.9.0.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.8.20-2
  Rebuilt with dependency generation.
