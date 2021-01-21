Name:       universal-packages-are-deprecated
Version:    1
Release:    2%{?dist}
Summary:    Universal packages are deprecated

License:    Public domain
BuildArch:  noarch

Obsoletes:  gettext-universal <= 0.21-4
Obsoletes:  glib2-universal <= 2.67.1-2
Obsoletes:  libffi-universal <= 3.3-4
Obsoletes:  libpcre-universal <= 8.44-4
Obsoletes:  libpixman-universal <= 0.40.0-3
Obsoletes:  libgpg-error-universal <= 1.41-2
Obsoletes:  libgcrypt-universal <= 1.8.7-5

%description

Universal packages were a failed experiment. If they return, it will be with
vastly different infrastructure. This package exists to prevent people from
installing old -universal packages by mistake.

%prep

%files

%changelog

* Thu Jan 21 2021 Morgan Thomas <m@m0rg.dev> 1-2
  Obsolete libgpg-error-universal, not libgpg-error...
