%define system_python 3.9

Name:           python-virtualenv
Version:        20.3.0
Release:        1%{?dist}
Summary:        Virtual Python Environment builder

License:        MIT
URL:            https://github.com/pypa/virtualenv
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/pypa/virtualenv.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/pypa/virtualenv.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot} --single-version-externally-managed

%files
%license LICENSE
%{_bindir}/virtualenv
%{_libdir}/python%{system_python}/site-packages/*

%changelog
