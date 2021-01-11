%define system_python 3.9

Name:           python-wheel
Version:        0.36.2
Release:        1%{?dist}
Summary:        A built-package format for Python

License:        Python-2.0
URL:            https://github.com/pypa/wheel
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/pypa/wheel.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/pypa/wheel .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%{_bindir}/wheel
%{_libdir}/python%{system_python}/site-packages/*

%changelog
