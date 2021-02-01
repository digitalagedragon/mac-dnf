%define system_python 3.9

Name:           python-certifi
Version:        2020.12.05
Release:        1%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle.

License:        MPL-2.0
URL:            https://github.com/certifi/python-certifi
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/certifi/python-certifi.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/certifi/python-certifi.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
