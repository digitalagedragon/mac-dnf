%define system_python 3.9

Name:           pivy
Version:        0.6.5
Release:        1%{?dist}
Summary:        Python bindings for coin3d

License:        ISC
URL:            https://github.com/coin3d/pivy
%undefine       _disable_source_fetch
Source0:        https://github.com/coin3d/pivy/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 16f2e339e5c59a6438266abe491013a20f53267e596850efad1559564a2c1719

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/coin3d/pivy.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+\\.\\d+)$" }

BuildRequires:  python%{system_python}
BuildRequires:  cmake
BuildRequires:  swig
BuildRequires:  libcoin-devel
BuildRequires:  libpython%{system_python}-devel

Requires:       libcoin

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
