%define system_python 3.9

Name:           python-filelock
Version:        3.0.12
Release:        1%{?dist}
Summary:        platform independent file locking

License:        Unlicense
URL:            https://github.com/benediktschmitt/py-filelock
%undefine       _disable_source_fetch
Source0:        https://github.com/benediktschmitt/py-filelock/archive/v%{version}.tar.gz#/python-filelock-%{version}.tar.gz
%define         SHA256SUM0 eafca6feda88295a054ccb3276adcc8d326318b116fa5e124522dd51dd62fd56

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/benediktschmitt/py-filelock.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n py-filelock-%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot} --single-version-externally-managed

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
