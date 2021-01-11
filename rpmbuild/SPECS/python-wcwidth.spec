%define system_python 3.9

Name:           python-wcwidth
Version:        0.2.5
Release:        1%{?dist}
Summary:        Library for building powerful interactive command lines in Python

License:        MIT
URL:            https://github.com/jquast/wcwidth
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/jquast/wcwidth.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/jquast/wcwidth.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
