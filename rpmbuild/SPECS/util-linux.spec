# this is basically only here for libsmartcols, use at your own risk
# may expand it eventually but most of util-linux (unsurprisingly) doesn't build on macOS

%define major_version 2.36
%define patch_version 1

Name:           util-linux
Version:        %{major_version}.%{patch_version}
Release:        1%{?dist}
Summary:        Various utility programs.

License:        GPLv2+, LGPLv2+, BSD
URL:            https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/
%undefine       _disable_source_fetch
Source0:        https://mirrors.edge.kernel.org/pub/linux/utils/%{name}/v%{major_version}/%{name}-%{version}.tar.xz
%define         SHA256SUM0 09fac242172cd8ec27f0739d8d192402c69417617091d8c6e974841568f37eed

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://git.kernel.org/pub/scm/utils/util-linux/util-linux.git",
# X10-Update-Spec:   "pattern": "^v((?:\\d+\\.?)+)$" }

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  libtool

%if "%{_build}" != "%{_host}"
%define host_tool_prefix %{_host}-
%endif

%description

%package     -n libsmartcols
Summary:        libsmartcols from util-linux
License:        GPLv2+, LGPLv2+, BSD
URL:            https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/
%description -n libsmartcols

%package     -n libsmartcols-devel
Summary:        Development files for libsmartcols
License:        GPLv2+, LGPLv2+, BSD
URL:            https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/
Requires:       libsmartcols = %{version}-%{release}
%description -n libsmartcols-devel

%package     -n libuuid
Summary:        libuuid from util-linux
License:        GPLv2+, LGPLv2+, BSD
URL:            https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/
%description -n libuuid

%package     -n libuuid-devel
Summary:        Development files for libuuid
License:        GPLv2+, LGPLv2+, BSD
URL:            https://mirrors.edge.kernel.org/pub/linux/utils/util-linux/
Requires:       libuuid = %{version}-%{release}
%description -n libuuid-devel

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n %{name}-%{version}

%build
#./autogen.sh
%configure --host=%{_target} --libdir=%{_prefix}/lib \
                --disable-all-programs \
                --disable-pylibmount \
                --disable-libmount   \
                --disable-static     \
                --enable-libsmartcols \
                --enable-libuuid \
                --without-python     \
                --without-systemd    \
                --without-systemdsystemunitdir
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang util-linux

%files -f util-linux.lang
%license COPYING README.licensing
%{_datadir}/bash-completion/completions/uuidgen
%doc %{_mandir}/man{1,5,8}/*

%files -n libsmartcols
%license COPYING README.licensing
%{_prefix}/lib/libsmartcols.*.dylib

%files -n libsmartcols-devel
%{_prefix}/lib/libsmartcols.dylib
%{_prefix}/lib/pkgconfig/smartcols.pc
%{_includedir}/libsmartcols

%files -n libuuid
%license COPYING README.licensing
%{_prefix}/lib/libuuid.*.dylib

%files -n libuuid-devel
%{_prefix}/lib/libuuid.dylib
%{_prefix}/lib/pkgconfig/uuid.pc
%{_includedir}/uuid
%doc %{_mandir}/man3/uuid*

%changelog
