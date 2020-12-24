Name:           xz
Version:        5.2.5
Release:        2%{?dist}
Summary:        XZ Utils is free general-purpose data compression software with a high compression ratio.

License:        GPLv2+
URL:            https://tukaani.org/xz/
%undefine       _disable_source_fetch
Source0:        https://tukaani.org/xz/xz-%{version}.tar.gz
%define         SHA256SUM0 f6f4910fd033078738bd82bfba4f49219d03b17eb0794eb91efbae419f4aba10

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://git.tukaani.org/xz.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

Requires: liblzma

%undefine _annotated_build

%description

%package     -n liblzma
Summary:        Libraries for LZMA compression and decompression.
License:        GPLv2+
URL:            https://tukaani.org/xz/

%description -n liblzma

%package     -n liblzma-devel
Summary:        Development files for liblzma
Requires:       liblzma%{?_isa} = %{version}-%{release}

%description -n liblzma-devel

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n xz-%{version}

%build
%configure --libdir=%{_prefix}/lib --host=%{_target} --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang xz

%files -f xz.lang
%license COPYING
%{_bindir}/*
%doc %{_mandir}/man1/*
%doc %{_mandir}/**/man1/*
%doc %{_datadir}/doc/xz

%files -n liblzma
%{_prefix}/lib/liblzma.*.dylib
%{_prefix}/lib/pkgconfig/liblzma.pc

%files -n liblzma-devel
%{_prefix}/lib/liblzma.dylib
%{_includedir}/lzma.h
%{_includedir}/lzma/

%changelog

* Wed Dec 23 2020 Morgan Thomas <m@m0rg.dev> 5.2.5-2
  Rebuilt with dependency generation.
