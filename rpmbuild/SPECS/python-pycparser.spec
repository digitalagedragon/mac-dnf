%define system_python 3.9

Name:           python-pycparser
Version:        2.20
Release:        1%{?dist}
Summary:        A Foreign Function Interface package for calling C libraries from Python

License:        MIT
URL:            https://github.com/eliben/pycparser
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/eliben/pycparser.git",
# X10-Update-Spec:   "pattern": "^release_v(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/eliben/pycparser.git .
git checkout release_v%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
