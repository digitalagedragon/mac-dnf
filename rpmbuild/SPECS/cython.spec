%define system_python 3.9

Name:           cython
Version:        0.29.21
Release:        1%{?dist}
Summary:        The fundamental package for scientific computing with Python

License:        Apache-2.0
URL:            https://cython.org/
%undefine       _disable_source_fetch
Source0:        https://files.pythonhosted.org/packages/6c/9f/f501ba9d178aeb1f5bf7da1ad5619b207c90ac235d9859961c11829d0160/Cython-%{version}.tar.gz
%define         SHA256SUM0 e57acb89bd55943c8d8bf813763d20b9099cc7165c0f16b707631a7654be9cad

BuildRequires:  python%{system_python}
BuildRequires:  libpython%{system_python}-devel
BuildRequires:  python-setuptools

Requires:       libpython%{system_python}-devel
Requires:       libpython%{system_python}
Requires:       python-setuptools

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}


%files
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/python%{system_python}/site-packages/*

%changelog
