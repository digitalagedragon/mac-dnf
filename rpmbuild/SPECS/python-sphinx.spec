%define system_python 3.9

Name:           python-sphinx
Version:        3.4.1
Release:        1%{?dist}
Summary:        A documentation tool

License:        MIT
URL:            https://www.sphinx-doc.org/en/master/
%undefine       _disable_source_fetch
Source0:        https://github.com/sphinx-doc/sphinx/archive/v%{version}.tar.gz#/sphinx-%{version}.tar.gz
%define         SHA256SUM0 96d8050a2f08efb58828c8923d96495778f663d92b888d5dda187ab7005ed213
BuildArch:      noarch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/sphinx-doc/sphinx.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

BuildRequires:  python%{system_python}
BuildRequires:  python-setuptools

Requires:       python-setuptools

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n sphinx-%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}


%files
%license LICENSE
%{_bindir}/*
%{_prefix}/lib/python%{system_python}/site-packages/*

%changelog

* Sat Dec 26 2020 Morgan Thomas <m@m0rg.dev> 3.4.1-1
  Updated to version 3.4.1.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.4.0-1
  Updated to version 3.4.0.
