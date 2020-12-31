%define pybasever 3.9
%define general_version %{pybasever}.1

Name:           python
Version:        %{general_version}
Release:        8%{?dist}
Summary:        The Python programming language

License:        Python-2.0
BuildArch:      noarch

Requires:       python%{pybasever}
Provides:       python(abi) = %{pybasever}

%description
Meta-package for system Python.

%package     -n libpython
Summary:        A library for embedding Python into other applications.
Requires:       libpython%{pybasever}

%description -n libpython
Meta-package for system libpython.

%package     -n libpython-devel
Summary:        Development files for libpython
Requires:       libpython%{pybasever}-devel

%description -n libpython-devel
Meta-package for system libpython-devel.

%install
%{__install} -dm755 %{buildroot}%{_bindir}

ln -sv 2to3-%{pybasever}         %{buildroot}%{_bindir}/2to3
ln -sv idle%{pybasever}          %{buildroot}%{_bindir}/idle3
ln -sv pydoc%{pybasever}         %{buildroot}%{_bindir}/pydoc3
ln -sv python%{pybasever}        %{buildroot}%{_bindir}/python3
ln -sv python%{pybasever}-config %{buildroot}%{_bindir}/python3-config
ln -sv python3                   %{buildroot}%{_bindir}/python

%files
%{_bindir}/*

%files -n libpython

%files -n libpython-devel

%changelog

* Thu Dec 31 2020 Morgan Thomas <m@m0rg.dev> 3.9.1-8
  Move the python3 symlinks into the unversioned package.
