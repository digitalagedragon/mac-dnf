%define system_python 3.9

Name:           python-babel
Version:        2.9.0
Release:        1%{?dist}
Summary:        Internationalization utilities

License:        BSD
URL:            http://babel.pocoo.org/en/latest/
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/python-babel/babel.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/python-babel/babel.git .
git checkout v%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_bindir}/pybabel
%{_libdir}/python%{system_python}/site-packages/*

%changelog
