%define system_python 3.9

Name:           python-cffi
Version:        1.14.4
Release:        1%{?dist}
Summary:        A Foreign Function Interface package for calling C libraries from Python

License:        MIT
URL:            https://foss.heptapod.net/pypy/cffi
%undefine       _disable_source_fetch
Source0:        https://files.pythonhosted.org/packages/66/6a/98e023b3d11537a5521902ac6b50db470c826c682be6a8c661549cb7717a/cffi-1.14.4.tar.gz

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://foss.heptapod.net/pypy/cffi",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

BuildRequires:  pkgconfig(python-%{system_python})

%description

%prep
%autosetup -n cffi-%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
