%define major_version 3.19
%define patch_version 1

Name:           cmake
Version:        %{major_version}.%{patch_version}
Release:        1%{?dist}
Summary:        The cmake build system

License:        BSD-3-Clause
URL:            https://cmake.org
%undefine       _disable_source_fetch
Source0:        https://github.com/Kitware/CMake/releases/download/v%{version}/%{name}-%{version}.tar.gz
%define         SHA256SUM0 1d266ea3a76ef650cdcf16c782a317cb4a7aa461617ee941e389cb48738a3aba

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/Kitware/CMake.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+\\.\\d+)$" }

%undefine _annotated_build
%global debug_package %{nil}

Provides: cmake%{major_version} = %{version}-%{release}

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

sed -e '/"lib64"/s/64//' -i.orig Modules/GNUInstallDirs.cmake

%build

%set_build_flags
./bootstrap --prefix=%{_prefix}
%make_build

%install
%make_install

mv %{buildroot}%{_prefix}/doc/cmake-%{major_version}/* %{buildroot}%{_datadir}/cmake-%{major_version}

%files
%license Copyright.txt
%{_bindir}/*

%{_datadir}/cmake-%{major_version}

%{_datadir}/aclocal/cmake.m4
%{_datadir}/bash-completion/completions/*
%{_datadir}/emacs/site-lisp/cmake-mode.el
%{_datadir}/vim/vimfiles/{indent,syntax}/cmake.vim

%changelog
