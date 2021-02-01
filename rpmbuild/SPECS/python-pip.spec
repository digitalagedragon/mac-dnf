%define system_python 3.9

Name:           python-pip
Version:        21.0
Release:        1%{?dist}
Summary:        The PyPA recommended tool for installing Python packages.

License:        MIT
URL:            https://pip.pypa.io/
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/pypa/pip.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

# RPM-Audit-Skip Audit::MacOSBinaryShadowing (expected package behavior)

%description

%prep
%setup -c -T
git clone https://github.com/pypa/pip.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/python%{system_python}/site-packages/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 21.0-1
  Updated to version 21.0.
