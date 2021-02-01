%define system_python 3.9

Name:           python-pytz
Version:        2020.5
Release:        1%{?dist}
Summary:        A configurable sidebar-enabled Sphinx theme

License:        MIT
URL:            https://pythonhosted.org/pytz/
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://git.launchpad.net/pytz",
# X10-Update-Spec:   "pattern": "^release_(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://git.launchpad.net/pytz .
git checkout release_%{version}

%build
make
cd src
python%{system_python} setup.py build

%install
cd src
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%{_libdir}/python%{system_python}/site-packages/*

%changelog
