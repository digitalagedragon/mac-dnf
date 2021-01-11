%define system_python 3.9

Name:           python-distlib
Version:        0.3.1
Release:        1%{?dist}
Summary:        Distribution utilities

License:        Python-2.0
URL:            https://bitbucket.org/pypa/distlib
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://bitbucket.org/pypa/distlib.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://bitbucket.org/pypa/distlib.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%{_libdir}/python%{system_python}/site-packages/*

%changelog
