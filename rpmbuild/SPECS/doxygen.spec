%define system_cmake 3.19

Name:           doxygen
Version:        1.8.20
Release:        1%{?dist}
Summary:        Documentation generator

License:        GPLv2
URL:            https://www.doxygen.org
%undefine       _disable_source_fetch
Source0:        https://doxygen.nl/files/doxygen-%{version}.src.tar.gz
%define         SHA256SUM0 e0db6979286fd7ccd3a99af9f97397f2bae50532e4ecb312aa18862f8401ddec

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
