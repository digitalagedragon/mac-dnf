%define system_python 3.9

Name:           python-ruamel-yaml-0.15
Version:        0.15.100
Release:        1%{?dist}
Summary:        ruamel.yaml is a YAML 1.2 loader/dumper package for Python.

License:        Python-2.0
URL:            https://github.com/pypa/wheel
%undefine       _disable_source_fetch
Source0:        https://files.pythonhosted.org/packages/9a/ee/55cd64bbff971c181e2d9e1c13aba9a27fd4cd2bee545dbe90c44427c757/ruamel.yaml-0.15.100.tar.gz
%define         SHA256SUM0 8e42f3067a59e819935a2926e247170ed93c8f0b2ab64526f888e026854db2e4

BuildRequires:  libpython%{system_python}-devel

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n ruamel.yaml-%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} -m pip install --root %{buildroot} --prefix %{_prefix} .

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
