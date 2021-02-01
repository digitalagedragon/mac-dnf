%define system_python 3.9

Name:           python-cryptography-2.9
Version:        2.9
Release:        1%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers

License:        Apache-2.0 or BSD
URL:            https://github.com/pyca/cryptography
%undefine       _disable_source_fetch

# this needs to be 2.9, not 2.9.2, because other packages have broken dependencies

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/pyca/cryptography.git",
# X10-Update-Spec:   "pattern": "^(2.9(?:\\.\\d+)?)$" }

BuildRequires:  pkgconfig(python-%{system_python})
BuildRequires:  pkgconfig(openssl)

%description

%prep
%setup -c -T
git clone https://github.com/pyca/cryptography.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
