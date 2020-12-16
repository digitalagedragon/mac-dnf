%define system_python 3.9

Name:           dnf
Version:        4.4.2
Release:        3%{?dist}
Summary:        A powerful RPM-based package manager

License:        GPLv2
URL:            https://github.com/rpm-software-management/dnf
%undefine       _disable_source_fetch
Source0:        https://github.com/rpm-software-management/dnf/archive/%{version}.tar.gz#/dnf-%{version}.tar.gz
%define         SHA256SUM0 175c4f4488c9263df026e16e8df610485b6a6aac6183321f13caf7585959ee14
#Source1:        dnf-01-etc-dnf-dnf.conf

Patch0:         dnf-0001-non-root.patch
Patch1:         dnf-0002-usrlocal.patch
Patch2:         dnf-0003-first-run-mark.patch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/rpm-software-management/dnf.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+\\.\\d+)$" }

BuildRequires:  librpm-devel
BuildRequires:  libsolv-devel
BuildRequires:  libdnf-devel
BuildRequires:  libcomps-devel
BuildRequires:  cmake
BuildRequires:  python%{system_python}

Requires:       rpm
Requires:       libsolv
Requires:       libcomps
Requires:       libdnf

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -p0

%build
mkdir build
cd build
cmake \
    -DPYTHON_EXECUTABLE:FILEPATH=/usr/local/bin/python%{system_python} \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPYTHON_DESIRED=3 -DWITH_MAN=0  ..
%make_build

%install
cd build
%make_install

ln -s dnf-3 %{buildroot}%{_bindir}/dnf
mv %{buildroot}%{_bindir}/dnf-automatic-3 %{buildroot}%{_bindir}/dnf-automatic
install -dm755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -dm755 %{buildroot}%{_localstatedir}/lib/dnf
#cp %SOURCE1 %{buildroot}%{_sysconfdir}/dnf/dnf.conf

mv %{buildroot}/etc/* %{buildroot}%{_sysconfdir}/

%find_lang dnf

%files -f build/dnf.lang
%license COPYING
%{_bindir}/*
%{_prefix}/lib/python%{system_python}/site-packages/dnf
%config %{_sysconfdir}/libreport
%config %{_sysconfdir}/dnf
%config %{_sysconfdir}/logrotate.d/dnf
%config %{_sysconfdir}/bash_completion.d/dnf
%dir %{_sysconfdir}/yum.repos.d
%dir %{_localstatedir}/lib/dnf

%exclude /usr/lib/tmpfiles.d
%exclude /usr/lib/systemd

%changelog
