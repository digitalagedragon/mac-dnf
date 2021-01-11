Name:           libflame
Version:        5.2.0
Release:        2%{?dist}
Summary:        A portable library for dense matrix computations

License:        BSD-3-Clause
URL:            https://www.cs.utexas.edu/~flame/web/libFLAME.html
%undefine       _disable_source_fetch
Source0:        https://github.com/flame/libflame/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 997c860f351a5c7aaed8deec00f502167599288fd0559c92d5bfd77d0b4d475c

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/flame/libflame.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

BuildRequires:  gcc

Requires:       gcc-libs

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%global osxflags %(echo "" %osxflags | sed -e 's/-Wpartial-availability//')
%configure --enable-lapack2flame
%make_build

%install
%make_install
mv %{buildroot}%{_libdir}/libflame{,-static}.a
cat >%{buildroot}%{_libdir}/libflame.a <<EOF
INPUT(-lflame-static -lz)
EOF

%files
# libflame builds a static library right now
# (it has a shared option and it doesn't work)

%files devel
%{_includedir}/FLAME.h
%{_libdir}/libflame-static.a
%{_libdir}/libflame.a
%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 5.2.0-2
  Rebuilt with dependency generation.
