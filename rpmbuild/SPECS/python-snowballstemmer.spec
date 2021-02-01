%define system_python 3.9

Name:           python-snowballstemmer
Version:        2.1.0
Release:        1%{?dist}
Summary:        This package provides 29 stemmers for 28 languages generated from Snowball algorithms.

License:        BSD-3-Clause
URL:            https://github.com/snowballstem/snowball
%undefine       _disable_source_fetch

Source0:        https://files.pythonhosted.org/packages/a3/3d/d305c9112f35df6efb51e5acd0db7009b74d86f35580e033451b5994a0a9/snowballstemmer-2.1.0.tar.gz

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/snowballstem/snowball.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%autosetup -n snowballstemmer-%{version}
#%setup -c -T
#git clone https://github.com/snowballstem/snowball.git .
#git checkout v%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license COPYING
%{_libdir}/python%{system_python}/site-packages/*

%changelog
