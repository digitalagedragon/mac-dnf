%define system_python 3.9

Name:           python-markupsafe
Version:        1.1.1
Release:        1%{?dist}
Summary:        Safely add untrusted strings to HTML/XML markup.

License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/pallets/markupsafe.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/pallets/markupsafe.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.rst
%{_libdir}/python%{system_python}/site-packages/*

%changelog
