# adapted from homebrew's

%define major 68
%define minor 1

Name:           libicu4c
Version:        %{major}.%{minor}
Release:        1%{?dist}
Summary:        C/C++ libraries for Unicode and Globalization

License:        ICU
URL:            http://site.icu-project.org/home
%undefine       _disable_source_fetch
Source0:        https://github.com/unicode-org/icu/releases/download/release-%{major}-%{minor}/icu4c-%{major}_%{minor}-src.tgz
%define         SHA256SUM0 a9f2e3d8b4434b8e53878b4308bd1e6ee51c9c7042e2b1a376abefb6fbb29f2d

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n icu/source -p0

%build
%configure --disable-samples --disable-tests --enable-static --with-library-bits=64
%make_build

%install
%make_install

%files
