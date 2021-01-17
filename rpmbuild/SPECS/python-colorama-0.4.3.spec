%define system_python 3.9

Name:           python-colorama-0.4.3
Version:        0.4.3
Release:        2%{?dist}
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

* Sun Jan 17 2021 Morgan Thomas <m@m0rg.dev> 0.4.3-2
  Explicitly call this python-colorama-0.4.3 to avoid DNF errors
