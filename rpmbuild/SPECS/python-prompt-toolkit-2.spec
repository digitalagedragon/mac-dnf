%define system_python 3.9

Name:           python-prompt-toolkit-2
Version:        2.0.10
Release:        1%{?dist}
Summary:        Library for building powerful interactive command lines in Python

License:        BSD
URL:            https://github.com/prompt-toolkit/python-prompt-toolkit
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/prompt-toolkit/python-prompt-toolkit.git",
# X10-Update-Spec:   "pattern": "^(2\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/prompt-toolkit/python-prompt-toolkit.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
