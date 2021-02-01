%define system_python 3.9

Name:           python-requests
Version:        2.25.1
Release:        1%{?dist}
Summary:        Python HTTP for Humans.

License:        Apache-2.0
URL:            https://requests.readthedocs.io/
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/psf/requests.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/psf/requests.git .
git checkout v%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
