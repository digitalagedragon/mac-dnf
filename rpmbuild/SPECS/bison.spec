Name:           bison
Version:        3.7.5
Release:        1%{?dist}
Summary:        A general-purpose parser generator

License:        GPLv3+
URL:            https://www.gnu.org/software/bison/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.xz
%define         SHA256SUM0 e8c53bc5bc396d636622d0f25e31ca92fd53f00b09629f13ef540d564a6b31ab

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/bison/"}

Provides:       gbison = %{version}-%{release}

%undefine _annotated_build

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build
%configure --bindir=%{_prefix}/opt/%{name}/bin --disable-static
%make_build

%install
%make_install

%find_lang %{name}
%find_lang %{name}-gnulib
%find_lang %{name}-runtime

rm -f %{buildroot}%{_infodir}/dir

%optlink

%optpost

%files -f %{name}.lang -f %{name}-gnulib.lang -f %{name}-runtime.lang
%license COPYING
%{_bindir}/*
%{_prefix}/opt/bison/bin/*
%exclude %{_prefix}/lib/liby.a
%{_datadir}/bison
%{_datadir}/aclocal/bison-i18n.m4
%doc %{_datadir}/doc/bison
%doc %{_infodir}/*.info*
%doc %{_mandir}/man1/*

%changelog

* Mon Jan 25 2021 Morgan Thomas <m@m0rg.dev> 3.7.5-1
  Updated to version 3.7.5.

* Sun Dec 27 2020 Morgan Thomas <m@m0rg.dev> 3.7.4-3
  Fix /usr/local/opt layout

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 3.7.4-2
  Rebuilt with dependency generation.
