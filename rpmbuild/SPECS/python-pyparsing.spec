%define system_python 3.9

Name:           python-pyparsing
Version:        2.4.7
Release:        1%{?dist}
Summary:        Python parsing module

License:        MIT
URL:            https://github.com/pyparsing/pyparsing
%undefine       _disable_source_fetch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/pyparsing/pyparsing.git",
# X10-Update-Spec:   "pattern": "^pyparsing_(\\d+\\.\\d+(?:\\.\\d+)?)$" }

%description

%prep
%setup -c -T
git clone https://github.com/pyparsing/pyparsing.git .
git checkout pyparsing_%{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot} --single-version-externally-managed

%files
%license LICENSE
%{_libdir}/python%{system_python}/site-packages/*

%changelog
