%define system_python 3.9

Name:           python-docutils
Version:        0.16
Release:        1%{?dist}
Summary:        Docutils -- Python Documentation Utilities

License:        BSD, GPLv3, Python-2.0, public domain
URL:            http://docutils.sourceforge.net/
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://repo.or.cz/docutils.git",
# X10-Update-Spec:   "pattern": "^docutils-(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://repo.or.cz/docutils.git .
git checkout docutils-%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license COPYING.txt
%{_bindir}/*
%{_libdir}/python%{system_python}/site-packages/*

%changelog
