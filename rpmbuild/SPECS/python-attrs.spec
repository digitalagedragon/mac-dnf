%define system_python 3.9

Name:           python-attrs
Version:        20.3.0
Release:        1%{?dist}
Summary:        Classes Without Boilerplate

License:        MIT
URL:            https://github.com/python-attrs/attrs
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/python-attrs/attrs.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/python-attrs/attrs.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
