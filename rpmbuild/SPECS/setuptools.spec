%define system_python 3.9

Name:           setuptools
Version:        51.1.0
Release:        2%{?dist}
Summary:        Easily download, build, install, upgrade, and uninstall Python packages

License:        MIT
URL:            https://pypi.org/project/setuptools/
%undefine       _disable_source_fetch
Source0:        https://github.com/pypa/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 2c175b6e818ef08cf195650dcd8650bbd416f122b2e8be11a5e018f196d37989
BuildArch:      noarch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/pypa/setuptools.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

# RPM-Audit-Skip Audit::MacOSBinaryShadowing (expected package behavior)

Provides:       python-setuptools = %{version}-%{release}

BuildRequires:  python%{system_python}

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
python%{system_python} ./bootstrap.py
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_bindir}/*
%{_prefix}/lib/python%{system_python}/site-packages/*

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 51.1.0-2
  Updated to version 51.1.0.
