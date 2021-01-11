%define system_python 3.9

Name:           python-distro
Version:        1.5.0
Release:        1%{?dist}
Summary:        Distro - an OS platform information API

License:        Apache-2.0
URL:            https://github.com/nir0s/distro
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/nir0s/distro.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/nir0s/distro.git .
git checkout v%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_bindir}/distro
%{_libdir}/python%{system_python}/site-packages/*

%changelog
