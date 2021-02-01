%define system_python 3.9

Name:           python-chardet
Version:        4.0.0
Release:        1%{?dist}
Summary:        Universal encoding detector for Python 2 and 3

License:        LGPL
URL:            https://github.com/chardet/chardet
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/chardet/chardet.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/chardet/chardet.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_bindir}/chardetect
%{_libdir}/python%{system_python}/site-packages/*

%changelog
