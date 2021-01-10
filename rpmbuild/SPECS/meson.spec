%define system_python 3.9

Name:           meson
Version:        0.56.1
Release:        2%{?dist}
Summary:        An efficient build system

License:        Apache-2.0
URL:            https://mesonbuild.com/
%undefine       _disable_source_fetch
Source0:        https://github.com/mesonbuild/meson/releases/download/%{version}/%{name}-%{version}.tar.gz
%define         SHA256SUM0 5780725304eaa28aac5e7de99d2d8d045112fbc10cf9f4181498b877de0ecf28
BuildArch:      noarch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/mesonbuild/meson.git",
# X10-Update-Spec:   "pattern": "^((?:\\d+\\.?)+)$" }

%if "%{_build}" != "%{_host}"
%define host_tool_prefix %{_host}-
%endif

BuildRequires:  python%{system_python}
BuildRequires:  python-setuptools

Requires:       python-setuptools
Requires:       python%{system_python}-%{name} = %{version}-%{release}

%undefine _annotated_build

%description

%package     -n python%{system_python}-%{name}
Summary:        Python %{system_python} bindings for %{name}
Provides:       python3-%{name} = %{version}-%{release}

%description -n python%{system_python}-%{name}

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license COPYING
%{_bindir}/meson
%{_datadir}/polkit-1/actions/*
%doc %{_mandir}/man1/meson*

%files -n python%{system_python}-%{name}
%{_prefix}/lib/python%{system_python}/site-packages/*

%changelog

* Sun Jan 10 2021 Morgan Thomas <m@m0rg.dev> 0.56.1-2
  Rebuilt with pythondistdeps generation.

* Wed Jan 06 2021 Morgan Thomas <m@m0rg.dev> 0.56.1-1
  Updated to version 0.56.1.
