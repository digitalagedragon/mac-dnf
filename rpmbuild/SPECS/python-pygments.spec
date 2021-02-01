%define system_python 3.9

Name:           python-pygments
Version:        2.7.4
Release:        1%{?dist}
Summary:        Pygments is a syntax highlighting package written in Python.

License:        BSD
URL:            https://pygments.org/
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/pygments/pygments.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/pygments/pygments.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_bindir}/pygmentize
%{_libdir}/python%{system_python}/site-packages/*

%changelog
