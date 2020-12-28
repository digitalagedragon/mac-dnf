%define pybasever 3.9
%define general_version %{pybasever}.1

Name:           python
Version:        %{general_version}
Release:        7%{?dist}
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

%files

%files -n libpython

%files -n libpython-devel

%changelog
