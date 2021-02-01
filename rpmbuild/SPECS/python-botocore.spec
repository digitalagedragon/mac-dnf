%define system_python 3.9

Name:           python-botocore
# tag your freakin' dev versions!
%define commit a0fa222e296e28b7dcb45944ba218fd3ccc6b25b
Version:        2.0.0dev89
Release:        1%{?dist}
Summary:        A low-level interface to a growing number of Amazon Web Services

License:        Apache-2.0
URL:            https://github.com/boto/botocore
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/boto/botocore.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

BuildRequires:  pkgconfig(python-%{system_python})

%description

%prep
%setup -c -T
git clone https://github.com/boto/botocore.git .
git checkout %{commit}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%{_libdir}/python%{system_python}/site-packages/*

%changelog

* Sun Jan 31 2021 Morgan Thomas <m@m0rg.dev> 2.0.0dev89
  Updated to version 2.0.0dev89.
