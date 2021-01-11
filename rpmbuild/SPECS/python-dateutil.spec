%define system_python 3.9

Name:           python-dateutil
Version:        2.8.1
Release:        1%{?dist}
Summary:        Extensions to the standard Python datetime module

License:        Apache-2.0 or 3-clause BSD
URL:            https://github.com/dateutil/dateutil
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/dateutil/dateutil.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/dateutil/dateutil.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
