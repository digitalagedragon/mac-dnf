Name:           neofetch
Version:        7.1.0
Release:        2%{?dist}
Summary:        Display system information

License:        MIT
URL:            https://github.com/dylanaraps/neofetch
%undefine       _disable_source_fetch
Source0:        https://github.com/dylanaraps/neofetch/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%define         SHA256SUM0 58a95e6b714e41efc804eca389a223309169b2def35e57fa934482a6b47c27e7
BuildArch:      noarch

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/dylanaraps/neofetch.git",
# X10-Update-Spec:   "pattern": "^(\\d+\\.\\d+(?:\\.\\d+)?)$" }

Patch0:         neofetch-0001-macos-rpm.patch

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version} -p0

%build

%install
%{__make} PREFIX=%{buildroot}/usr/local install

%files
%{_bindir}/neofetch
%doc %{_mandir}/man1/*
