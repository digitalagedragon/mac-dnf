%define system_python 3.9

Name:           python-prompt-toolkit
Version:        3.0.14
Release:        1%{?dist}
Summary:        Library for building powerful interactive command lines in Python

License:        BSD
URL:            https://github.com/prompt-toolkit/python-prompt-toolkit
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/prompt-toolkit/python-prompt-toolkit.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

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

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 3.0.14-1
  Updated to version 3.0.14.
