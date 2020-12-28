%define major_version 3.19
%define patch_version 2

Name:           cmake
Version:        %{major_version}.%{patch_version}
Release:        4%{?dist}
Summary:        The cmake build system

License:        BSD-3-Clause
BuildArch:      noarch

Requires:       cmake%{major_version}

%description
Meta-package for system CMake.

%files

%changelog
