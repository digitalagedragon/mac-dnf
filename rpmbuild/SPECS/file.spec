Name:           file
Version:        5.39
Release:        3%{?dist}
Summary:        A utility for determining the type of a file.

License:        BSD-2-Clause
URL:            http://astron.com/pub/file/
%undefine       _disable_source_fetch
Source0:        http://astron.com/pub/%{name}/%{name}-%{version}.tar.gz
%define         SHA256SUM0 f05d286a76d9556243d0cb05814929c2ecf3a5ba07963f8f70bfaaa70517fad1

# X10-Update-Spec: { "type": "webscrape", "url": "http://astron.com/pub/file/"}

%description

%package     -n libmagic
Summary:        file(1), but library
License:        BSD-2-Clause
URL:            http://astron.com/pub/file/

%description -n libmagic

%package     -n libmagic-devel
Summary:        Development files for libmagic
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n libmagic-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version}

%build
%configure --bindir=%{_prefix}/opt/%{name}/bin
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%posttrans
echo Note: macOS provides its own %{name}, so %{name}\\'s binaries have been installed under /usr/local/opt/%{name}/bin.

%files
%license COPYING
%{_prefix}/opt/%{name}/bin/file
%doc %{_mandir}/man1/*

%files -n libmagic
%{_datadir}/misc/magic.mgc
%{_prefix}/lib/libmagic.*.dylib
%doc %{_mandir}/man4/*

%files -n libmagic-devel
%{_prefix}/lib/libmagic.dylib
%{_prefix}/lib/pkgconfig/libmagic.pc
%{_includedir}/magic.h
%doc %{_mandir}/man3/*

%changelog

* Thu Dec 31 2020 Morgan Thomas <m@m0rg.dev> 5.39-3
  Move the file binary to /usr/local/opt to avoid conflicting with macOS-provided file.
  
* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 5.39-2
  Rebuilt with dependency generation.
