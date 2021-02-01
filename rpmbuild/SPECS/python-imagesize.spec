%define system_python 3.9

Name:           python-imagesize
Version:        1.1.0
Release:        1%{?dist}
Summary:        Getting image size from png/jpeg/jpeg2000/gif file

License:        MIT
URL:            https://github.com/shibukawa/imagesize_py
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/shibukawa/imagesize_py.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/shibukawa/imagesize_py.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.rst
%{_libdir}/python%{system_python}/site-packages/*

%changelog
