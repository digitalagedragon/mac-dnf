%define system_python 3.9

Name:           numpy
Version:        1.19.5
Release:        2%{?dist}
Summary:        The fundamental package for scientific computing with Python

License:        BSD-3-Clause
URL:            https://numpy.org/
%undefine       _disable_source_fetch
Source0:        https://github.com/numpy/numpy/releases/download/v%{version}/numpy-%{version}.tar.gz
%define         SHA256SUM0 d1654047d75fb9d55cc3d46f312d5247eec5f4999039874d2f571bb8021d8f0b

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/numpy/numpy.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+\\.\\d+)$" }

BuildRequires:  python%{system_python}
BuildRequires:  python%{system_python}dist(cython)
BuildRequires:  python-setuptools

Requires:       python-setuptools
Requires:       python%{system_python}dist(cython)

Provides:       python3-%{name} = %{version}-%{release}
Provides:       python%{system_python}-%{name} = %{version}-%{release}

%ifarch x86_64
# Accelerate.framework is really buggy on x86_64, so we need to use some
# other BLAS/LAPACK library. I'd like to be able to do this on any architecture
# for consistency but I can't build a gfortran that works on aarch64 right now.
BuildRequires:  libflame-devel
BuildRequires:  gcc
Requires:       libflame
Requires:       gcc-libs
%endif

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%ifarch aarch64
# this is all kinds of weird on aarch64, not helped by the fact that
# I can't build any kind of BLAS/LAPACK for aarch64 yet (because no gfortran)
# basically the script assumes that if you're building against Accelerate.framework
# (macOS's packaged BLAS libraries, which I have to use on aarch64) and you're not on
# intel, you're clearly on an old macOS with an old compiler that it can pass
# -faltivec to and have it not blow up.
# this is not a good assumption.
sed -e 's/-faltivec//' -I.orig numpy/distutils/system_info.py
%endif

%build
# numpy doesn't like split build/install steps
#python%{system_python} setup.py build

%install
%ifarch x86_64
export CC=/usr/local/bin/gcc
%endif
python%{system_python} setup.py build install --root %{buildroot} --single-version-externally-managed

%files
%license LICENSE.txt
%{_bindir}/*
%{_libdir}/python%{system_python}/site-packages/*

%changelog

* Sun Jan 10 2021 Morgan Thomas <m@m0rg.dev> 1.19.5-2
  Rebuilt with pythondistdeps generation.

* Wed Jan 06 2021 Morgan Thomas <m@m0rg.dev> 1.19.5-1
  Updated to version 1.19.5.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.19.4-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 1.19.4-1
  Updated to version 1.19.4.
