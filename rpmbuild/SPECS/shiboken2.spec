%define system_python 3.9

Name:           shiboken2
Version:        5.15.2
Release:        1%{?dist}
Summary:        GeneratorRunner plugin that outputs C++ code for CPython extensions

License:        LGPLv3, GPLv3, GPLv2, FDL
URL:            https://wiki.qt.io/Qt_for_Python
Source0:        pyside2-%{version}.tar.gz

BuildRequires:  python%{system_python}
BuildRequires:  libpython%{system_python}-devel
BuildRequires:  libqt-devel
BuildRequires:  cmake
BuildRequires:  llvm
BuildRequires:  numpy
BuildRequires:  python-sphinx

Requires:       libqt
Requires:       libclang

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libclang

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n pyside2-%{version}

%build
mkdir build
cd build
cmake -Wno-dev -DCMAKE_BUILD_TYPE=Release \
    -DPYTHON_DESIRED=3 \
    -DPYTHON_EXECUTABLE:FILEPATH=/usr/local/bin/python%{system_python} \
    -DPYTHON_LIBRARY=/usr/local/lib/libpython%{system_python}.dylib \
    -DPYTHON_INCLUDE_DIR=/usr/local/include/python%{system_python} \
    -DBUILD_TESTS=Release \
    -DBUILD_TESTS:BOOL=OFF \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ../sources/shiboken2
%make_build

%install
cd build
%make_install

%files
%license LICENSE.FDL LICENSE.GPL2 LICENSE.GPLv3 LICENSE.LGPLv3
%{_libdir}/libshiboken2.cpython-*-darwin.*.dylib

%files devel
%{_bindir}/shiboken2
%{_bindir}/shiboken_tool.py
%{_includedir}/shiboken2
%{_libdir}/cmake/Shiboken2-%{version}
%{_libdir}/libshiboken2.cpython-*-darwin.dylib
%{_libdir}/pkgconfig/shiboken2.pc
%{_libdir}/python%{system_python}/site-packages/*

%changelog
