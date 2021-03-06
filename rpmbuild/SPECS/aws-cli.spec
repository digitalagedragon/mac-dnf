%define system_python 3.9

Name:           aws-cli
Version:        2.1.21
Release:        1%{?dist}
Summary:        Official AWS command-line interface

License:        MIT
URL:            https://github.com/aws/aws-cli
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/aws/aws-cli.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/aws/aws-cli.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/python%{system_python}/site-packages/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 2.1.21-1
  Updated to version 2.1.21.
