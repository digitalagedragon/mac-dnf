%define system_python 3.9

Name:           python-tox
Version:        3.13.2
Release:        1%{?dist}
Summary:        virtualenv management tool

License:        MIT
URL:            http://tox.readthedocs.org/
%undefine       _disable_source_fetch
Source0:        https://github.com/tox-dev/tox/archive/%{version}.tar.gz#/python-tox-%{version}.tar.gz
%define         SHA256SUM0 89967cad79e09d8e78dcfd2a43c80214048b976e1d490db6fa19d8d5968da5df

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/tox-dev/tox.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n tox-%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot} --single-version-externally-managed

%files
%license LICENSE
%{_bindir}/tox
%{_bindir}/tox-quickstart
%{_libdir}/python%{system_python}/site-packages/*

%changelog
