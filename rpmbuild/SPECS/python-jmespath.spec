%define system_python 3.9

Name:           python-jmespath
Version:        0.10.0
Release:        1%{?dist}
Summary:        JSON Matching Expressions

License:        MIT
URL:            https://github.com/jmespath/jmespath.py
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/jmespath/jmespath.py.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/jmespath/jmespath.py.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%{_bindir}/jp.py
%{_libdir}/python%{system_python}/site-packages/*

%changelog
