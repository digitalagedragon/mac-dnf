%define system_python 3.9

Name:           python-s3transfer
Version:        0.3.4
Release:        1%{?dist}
Summary:        An Amazon S3 Transfer Manager

License:        Apache-2.0
URL:            https://github.com/boto/s3transfer
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/boto/s3transfer.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/boto/s3transfer.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%{_libdir}/python%{system_python}/site-packages/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 0.3.4-1
  Updated to version 0.3.4.
