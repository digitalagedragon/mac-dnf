%define system_python 3.9

Name:           matplotlib
Version:        3.3.3
Release:        1%{?dist}
Summary:        Python visualization library

License:        MIT
URL:            https://matplotlib.org/
%undefine       _disable_source_fetch
Source0:        https://files.pythonhosted.org/packages/7b/b3/7c48f648bf83f39d4385e0169d1b68218b838e185047f7f613b1cfc57947/matplotlib-3.3.3.tar.gz
%define         SHA256SUM0 b1b60c6476c4cfe9e5cf8ab0d3127476fd3d5f05de0f343a452badaad0e4bdec

BuildRequires:  python%{system_python}
BuildRequires:  libpython%{system_python}-devel
BuildRequires:  python-setuptools
BuildRequires:  numpy
BuildRequires:  libfreetype-devel

Requires:       python-setuptools
Requires:       numpy
Requires:       libfreetype

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --root %{buildroot}


%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
