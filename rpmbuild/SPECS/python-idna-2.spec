%define system_python 3.9

Name:           python-idna-2
Version:        2.10
Release:        1%{?dist}
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        BSD-3-Clause
URL:            https://github.com/kjd/idna
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/kjd/idna.git",
# X10-Update-Spec:   "pattern": "^v(2\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/kjd/idna.git .
git checkout v%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.rst
%{_libdir}/python%{system_python}/site-packages/*

%changelog
