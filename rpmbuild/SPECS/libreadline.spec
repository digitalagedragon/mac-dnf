Name:           libreadline
Version:        8.1
Release:        4%{?dist}
Summary:        Command line editing library

License:        GPLv3+
URL:            https://www.gnu.org/software/readline
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/readline/readline-%{version}.tar.gz
%define         SHA256SUM0 f8ceb4ee131e3232226a17f51b164afc46cd0b9e6cef344be87c65962cb82b02

# X10-Update-Spec: { "type": "webscrape", "url": "https://ftp.gnu.org/gnu/readline/"}

# TODO that should be PREFIX=/usr/local/opt/readline, not /usr/local/opt...
%description

Note: macOS provides its own -lreadline, so this installs libraries into /usr/local/opt/lib.
Anything using pkg-config shouldn't have trouble with it.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n readline-%{version}

%build

%configure --libdir=%{_prefix}/opt/lib --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%{__install} -dm755 %{buildroot}%{_libdir}
mv %{buildroot}%{_prefix}/opt/lib/pkgconfig %{buildroot}%{_libdir}
sed -e 's/Requires.private: termcap//' -I "" %{buildroot}%{_libdir}/pkgconfig/readline.pc

%files
%{_prefix}/opt/lib/libhistory.*.dylib
%{_prefix}/opt/lib/libreadline.*.dylib

%files devel
%{_includedir}/readline
%{_prefix}/opt/lib/libhistory.dylib
%{_prefix}/opt/lib/libreadline.dylib
%{_libdir}/pkgconfig/*.pc
%doc %{_mandir}/man3/*
%doc %{_infodir}/*
%doc %{_docdir}/readline

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 8.1-4
  Rebuilt with dependency generation.
