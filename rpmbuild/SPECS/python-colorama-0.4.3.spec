%define system_python 3.9

Name:           python-colorama
Version:        0.4.3
Release:        1%{?dist}
Summary:        Library for building powerful interactive command lines in Python

License:        BSD
URL:            https://github.com/tartley/colorama
%undefine       _disable_source_fetch

%description

%prep
%setup -c -T
git clone https://github.com/tartley/colorama.git .
git checkout %{version}

%build
python%{system_python} setup.py build

%install
python%{system_python} setup.py install --skip-build --root %{buildroot}

%files
%license LICENSE.txt
%{_libdir}/python%{system_python}/site-packages/*

%changelog
