%define system_python 3.9

Name:           setuptools
Version:        51.1.1
Release:        2%{?dist}
Summary:        Easily download, build, install, upgrade, and uninstall Python packages

License:        MIT
URL:            https://pypi.org/project/setuptools/
%undefine       _disable_source_fetch
Source0:        https://github.com/pypa/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 97434f60d427e33cbcbd69003a20596f66a8643079858a8768574a8b73a97dbd
BuildArch:      noarch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/pypa/setuptools.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

# RPM-Audit-Skip Audit::MacOSBinaryShadowing (expected package behavior)

Requires:       python%{system_python}-%{name} = %{version}-%{release}

%package     -n python%{system_python}-%{name}
Summary:        Python %{system_python} bindings for %{name}
Provides:       python3-%{name} = %{version}-%{release}
Provides:       python-setuptools = %{version}-%{release}

%description -n python%{system_python}-%{name}

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

%files -n python%{system_python}-%{name}
%{_prefix}/lib/python%{system_python}/site-packages/*

%changelog

* Sun Jan 10 2021 Morgan Thomas <m@m0rg.dev> 51.1.1-2
  Rebuilt with pythondistdeps generation.

* Thu Dec 31 2020 Morgan Thomas <m@m0rg.dev> 51.1.1-1
  Updated to version 51.1.1.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 51.1.0-2
  Updated to version 51.1.0.
