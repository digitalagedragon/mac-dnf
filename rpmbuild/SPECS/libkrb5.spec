%define major_version 1.18
%define patch_version 3

Name:           libkrb5
Version:        %{major_version}.%{patch_version}
Release:        1%{?dist}
Summary:        Network authentication protocol

License:        MIT
URL:            https://web.mit.edu/kerberos/
%undefine       _disable_source_fetch
Source0:        https://kerberos.org/dist/krb5/%{major_version}/krb5-%{version}.tar.gz
%define         SHA256SUM0 e61783c292b5efd9afb45c555a80dd267ac67eebabca42185362bee6c4fbd719

BuildRequires:  pkgconfig(libssl)

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n krb5
Summary:        Command-line tools and utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n krb5

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -n krb5-%{version}

# Newer versions of clang are very picky about missing includes.
# One configure test fails because it doesn't #include the header needed
# for some functions used in the rest. The test isn't actually testing
# those functions, just using them for the feature they're
# actually testing. Adding the include fixes this.
# https://krbdev.mit.edu/rt/Ticket/Display.html?id=8928

sed -I.orig -e "/^void foo1() __attribute__((constructor));/i\ 
#include <unistd.h>" src/configure

%build
cd src
%configure \
    --bindir=%{_prefix}/opt/%{name}/bin \
    --sbindir=%{_prefix}/opt/%{name}/sbin \
    --libdir=%{_prefix}/opt/%{name}/lib \
    --without-system-verto \
    --without-keyutils

%make_build

%install
cd src
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fv %{buildroot}%{_infodir}/dir

%{__install} -dm755 %{buildroot}%{_libdir}/pkgconfig
for f in $(ls %{buildroot}%{_prefix}/opt/%{name}/lib/pkgconfig); do
    ln -sfv %{_prefix}/opt/%{name}/lib/pkgconfig/$f %{buildroot}%{_libdir}/pkgconfig/$f
done

%find_lang mit-krb5

%posttrans
echo Note: macOS provides its own %{name}, so %{name}\\'s binaries have been installed under /usr/local/opt/%{name}/bin.
echo Note: macOS provides its own %{name}, so %{name}\\'s libraries have been installed under /usr/local/opt/%{name}/lib.

%files -f src/mit-krb5.lang
%{_prefix}/opt/%{name}/lib/krb5
%{_prefix}/opt/%{name}/lib/libcom_err.*.dylib
%{_prefix}/opt/%{name}/lib/libgssapi_krb5.*.dylib
%{_prefix}/opt/%{name}/lib/libgssrpc.*.dylib
%{_prefix}/opt/%{name}/lib/libk5crypto.*.dylib
%{_prefix}/opt/%{name}/lib/libkadm5clnt_mit.*.dylib
%{_prefix}/opt/%{name}/lib/libkadm5srv_mit.*.dylib
%{_prefix}/opt/%{name}/lib/libkdb5.*.dylib
%{_prefix}/opt/%{name}/lib/libkrad.*.dylib
%{_prefix}/opt/%{name}/lib/libkrb5.*.dylib
%{_prefix}/opt/%{name}/lib/libkrb5support.*.dylib
%{_prefix}/opt/%{name}/lib/libverto.*.dylib

%files devel
%{_includedir}/com_err.h
%{_includedir}/gssapi.h
%{_includedir}/gssapi
%{_includedir}/gssrpc
%{_includedir}/kadm5
%{_includedir}/kdb.h
%{_includedir}/krad.h
%{_includedir}/krb5.h
%{_includedir}/krb5
%{_includedir}/profile.h
%{_includedir}/verto-module.h
%{_includedir}/verto.h
%{_prefix}/opt/%{name}/bin/krb5-config
%{_prefix}/opt/%{name}/lib/libcom_err.dylib
%{_prefix}/opt/%{name}/lib/libgssapi_krb5.dylib
%{_prefix}/opt/%{name}/lib/libgssrpc.dylib
%{_prefix}/opt/%{name}/lib/libk5crypto.dylib
%{_prefix}/opt/%{name}/lib/libkadm5clnt_mit.dylib
%{_prefix}/opt/%{name}/lib/libkadm5clnt.dylib
%{_prefix}/opt/%{name}/lib/libkadm5srv_mit.dylib
%{_prefix}/opt/%{name}/lib/libkadm5srv.dylib
%{_prefix}/opt/%{name}/lib/libkdb5.dylib
%{_prefix}/opt/%{name}/lib/libkrad.dylib
%{_prefix}/opt/%{name}/lib/libkrb5.dylib
%{_prefix}/opt/%{name}/lib/libkrb5support.dylib
%{_prefix}/opt/%{name}/lib/libverto.dylib
%{_prefix}/opt/%{name}/lib/pkgconfig/*.pc
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/krb5-config*
%{_mandir}/man5/*
%{_mandir}/man5/.*

%files -n krb5
%{_prefix}/opt/%{name}/bin/compile_et
%{_prefix}/opt/%{name}/bin/gss-client
%{_prefix}/opt/%{name}/bin/k5srvutil
%{_prefix}/opt/%{name}/bin/kadmin
%{_prefix}/opt/%{name}/bin/kdestroy
%{_prefix}/opt/%{name}/bin/kinit
%{_prefix}/opt/%{name}/bin/klist
%{_prefix}/opt/%{name}/bin/kpasswd
%{_prefix}/opt/%{name}/bin/kswitch
%{_prefix}/opt/%{name}/bin/ktutil
%{_prefix}/opt/%{name}/bin/kvno
%{_prefix}/opt/%{name}/bin/sclient
%{_prefix}/opt/%{name}/bin/sim_client
%{_prefix}/opt/%{name}/bin/uuclient
%{_prefix}/opt/%{name}/sbin/*
%{_datadir}/et
%{_mandir}/man1/compile_et.1*
%{_mandir}/man1/k5srvutil.1*
%{_mandir}/man1/kadmin.1*
%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/kpasswd.1*
%{_mandir}/man1/krb5-config.1*
%{_mandir}/man1/ksu.1*
%{_mandir}/man1/kswitch.1*
%{_mandir}/man1/ktutil.1*
%{_mandir}/man1/kvno.1*
%{_mandir}/man1/sclient.1*
%{_mandir}/man7/*
%{_mandir}/man8/*
%{_datadir}/examples/krb5

%changelog
