%define system_python 3.9

Name:           pyside2
Version:        5.15.2
Release:        1%{?dist}
Summary:        Python bindings for libqt

License:        LGPLv3, GPLv3, GPLv2, FDL, BSD
URL:            https://wiki.qt.io/Qt_for_Python
%undefine       _disable_source_fetch
Source0:        https://download.qt.io/official_releases/QtForPython/pyside2/PySide2-%{version}-src/pyside-setup-opensource-src-%{version}.tar.xz
%define         SHA256SUM0 b306504b0b8037079a8eab772ee774b9e877a2d84bab2dbefbe4fa6f83941418

BuildRequires:  python%{system_python}
BuildRequires:  libpython%{system_python}-devel
BuildRequires:  libqt-devel
BuildRequires:  cmake
BuildRequires:  python-sphinx
BuildRequires:  llvm

Requires:       libqt

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel libopenssl-devel
Requires:       libxml2-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n shiboken2
Summary:        Python bindings generator for libqt
Requires:       libclang
Requires:       libqt

%description -n shiboken2

%package -n shiboken2-devel
Summary:        Development files for shiboken2
Requires:       shiboken2%{?_isa} = %{version}-%{release}
Requires:       libcurl-devel libopenssl-devel
Requires:       libxml2-devel

%description -n shiboken2-devel
The shiboken2-devel package contains libraries and header files for
developing applications that use shiboken2.

%package tools
Summary:        Command-line tools and utilities for pyside2
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n pyside-setup-opensource-src-%{version}

%build
mkdir build
cd build

export CFLAGS="-I/usr/local/include/QtUiTools"
export CXXFLAGS="-I/usr/local/include/QtUiTools"
cmake -Wno-dev -DCMAKE_BUILD_TYPE=Release \
    -DUSE_PYTHON_VERSION=3 \
    -DPYTHON_EXECUTABLE:FILEPATH=/usr/local/bin/python%{system_python} \
    -DPYTHON_LIBRARY=/usr/local/lib/libpython%{system_python}.dylib \
    -DPYTHON_INCLUDE_DIR=/usr/local/include/python%{system_python} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
cmake --build . %{?_smp_mflags}

%install
cd build
%make_install

%files
%license LICENSE.FDL LICENSE.GPL2 LICENSE.GPLv3 LICENSE.LGPLv3
%{_libdir}/libpyside2.cpython-*-darwin.*.dylib
%{_libdir}/python%{system_python}/site-packages/PySide2

%files devel
%{_libdir}/libpyside2.cpython-*-darwin.dylib
%{_libdir}/cmake/PySide2-%{version}
%{_libdir}/pkgconfig/pyside2.pc
%{_includedir}/PySide2/
%{_datadir}/PySide2/

%files -n shiboken2
%{_bindir}/shiboken2
%{_bindir}/shiboken_tool.py
%{_libdir}/libshiboken2.cpython-*-darwin.*.dylib
%{_libdir}/python%{system_python}/site-packages/shiboken2

%files -n shiboken2-devel
%{_libdir}/libshiboken2.cpython-*-darwin.dylib
%{_libdir}/python%{system_python}/site-packages/shiboken2_generator
%{_libdir}/cmake/Shiboken2-%{version}
%{_libdir}/pkgconfig/shiboken2.pc
%{_includedir}/shiboken2

%files tools
%{_bindir}/pyside2-lupdate
%{_bindir}/pyside_tool.py
%{_mandir}/man1/*
# why are these even written... they should be part of libqt iirc
%exclude %{_bindir}/rcc
%exclude %{_bindir}/uic
%exclude %{_bindir}/Designer.app

%changelog
