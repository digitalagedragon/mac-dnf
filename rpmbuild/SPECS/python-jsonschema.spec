%define system_python 3.9

Name:           python-jsonschema
Version:        3.2.0
Release:        1%{?dist}
Summary:        An implementation of JSON Schema validation for Python

License:        MIT
URL:            https://github.com/Julian/jsonschema
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/Julian/jsonschema.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/Julian/jsonschema.git .
git checkout v%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license COPYING
%{_bindir}/jsonschema
%{_libdir}/python%{system_python}/site-packages/*

%changelog
