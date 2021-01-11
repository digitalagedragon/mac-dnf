%define system_python 3.9

Name:           python-appdirs
Version:        1.4.4
Release:        1%{?dist}
Summary:        A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir".

License:        MIT
URL:            http://github.com/ActiveState/appdirs
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "http://github.com/ActiveState/appdirs.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone http://github.com/ActiveState/appdirs.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot} --single-version-externally-managed

%files
%license LICENSE.txt
%{_libdir}/python%{system_python}/site-packages/*

%changelog
