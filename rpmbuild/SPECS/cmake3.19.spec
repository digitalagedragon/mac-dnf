%define major_version 3.19
%define patch_version 2

%define is_system_cmake 1

Name:           cmake%{major_version}
Version:        %{major_version}.%{patch_version}
Release:        3%{?dist}
Summary:        The cmake build system

License:        BSD-3-Clause
URL:            https://cmake.org
%undefine       _disable_source_fetch
Source0:        https://github.com/Kitware/CMake/releases/download/v%{version}/cmake-%{version}.tar.gz
%define         SHA256SUM0 e3e0fd3b23b7fb13e1a856581078e0776ffa2df4e9d3164039c36d3315e0c7f0

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/Kitware/CMake.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+\\.\\d+)$" }

%undefine _annotated_build
%global debug_package %{nil}

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n cmake-%{version}

sed -e '/"lib64"/s/64//' -i.orig Modules/GNUInstallDirs.cmake

%build

%set_build_flags
./bootstrap --prefix=%{_prefix}
%make_build

%install
%make_install

mv %{buildroot}%{_prefix}/doc/cmake-%{major_version}/* %{buildroot}%{_datadir}/cmake-%{major_version}
for f in $(ls %{buildroot}%{_bindir}); do
    mv %{buildroot}%{_bindir}/$f %{buildroot}%{_bindir}/${f}%{major_version}
%if %{is_system_cmake}
    ln -s $(basename $f)%{major_version} %{buildroot}%{_bindir}/$f
%endif
done

%files
%license Copyright.txt
%{_bindir}/*

%{_datadir}/cmake-%{major_version}

%if %{is_system_cmake}
%{_datadir}/aclocal/cmake.m4
%{_datadir}/bash-completion/completions/*
%{_datadir}/emacs/site-lisp/cmake-mode.el
%{_datadir}/vim/vimfiles/{indent,syntax}/cmake.vim
%else
%exclude %{_datadir}/aclocal/cmake.m4
%exclude %{_datadir}/bash-completion/completions/*
%exclude %{_datadir}/emacs/site-lisp/cmake-mode.el
%exclude %{_datadir}/vim/vimfiles/{indent,syntax}/cmake.vim
%endif

%changelog

* Sun Dec 27 2020 Morgan Thomas <m@m0rg.dev> 3.19.2-3
  Infrastructure changes.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.19.2-2
  Rebuilt with dependency generation.

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.19.2-1
  Updated to version 3.19.2.

* Thu Dec 17 2020 Morgan Thomas <m@morg.dev> 3.19.1-2
  Infrastructure for multiple cmake versions.
