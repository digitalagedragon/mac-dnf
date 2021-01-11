%define system_python 3.9

Name:           python-pyrsistent
Version:        0.17.3
Release:        1%{?dist}
Summary:        Persistent/Functional/Immutable data structures

License:        MIT
URL:            http://github.com/tobgu/pyrsistent
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "http://github.com/tobgu/pyrsistent.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+(?:\\.\\d+)?)$" }

BuildRequires:  libpython%{system_python}-devel

%description

%prep
%setup -c -T
git clone http://github.com/tobgu/pyrsistent.git .
git checkout v%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENCE.mit
%{_libdir}/python%{system_python}/site-packages/*

%changelog
