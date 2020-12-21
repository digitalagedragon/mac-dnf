%define system_python 3.9

Name:           numpy
Version:        1.19.0
Release:        1%{?dist}
Summary:         The fundamental package for scientific computing with Python

License:        BSD-3-Clause
URL:            https://numpy.org/
%undefine       _disable_source_fetch
Source0:        https://github.com/numpy/numpy/releases/download/v%{version}/numpy-%{version}.tar.gz
%define         SHA256SUM0 153cf8b0176e57a611931981acfe093d2f7fef623b48f91176efa199798a6b90

BuildRequires:  python%{system_python}
BuildRequires:  cython
BuildRequires:  python-setuptools

Requires:       python-setuptools

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

# this is all kinds of weird on aarch64, not helped by the fact that
# I can't build OpenBLAS for aarch64 yet (it needs GCC)
# basically the script assumes that if you're building against Accelerate.framework
# (macOS's packaged BLAS libraries, which I have to use on aarch64) and you're not on
# intel, you're clearly on an old macOS with an old compiler that it can pass
# -faltivec to and have it not blow up.
# this is not a good assumption.
sed -e 's/-faltivec//' -I.orig numpy/distutils/system_info.py

%build
# numpy doesn't like split build/install steps
#python%{system_python} setup.py build

%install
python%{system_python} setup.py build install --root %{buildroot} --single-version-externally-managed


%files
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/python%{system_python}/site-packages/*

%changelog
