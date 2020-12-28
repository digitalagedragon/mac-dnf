Name:           emacs
Version:        27.1
Release:        1%{?dist}
Summary:        The GNU Emacs text editor

License:        GPLv3+
URL:            https://www.gnu.org/software/emacs/
%undefine       _disable_source_fetch
Source0:        https://ftp.gnu.org/gnu/emacs/emacs-27.1.tar.xz
%define         SHA256SUM0 4a4c128f915fc937d61edfc273c98106711b540c9be3cd5d2e2b9b5b2f172e41

Patch0:         https://raw.githubusercontent.com/Homebrew/formula-patches/25c1e1797d4004a9e5b9453779399afc63d04b97/emacs/arm.patch#/emacs-0001-aarch64.patch

BuildRequires:  xz
BuildRequires:  pkgconfig(gnutls)

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup -p1

%build
%configure \
    --without-x \
    --with-xml2 \
    --without-dbus \
    --with-modules \
    --without-ns \
    --without-imagemagick \
    --with-dumping=none \
    --with-pdumper=no

%make_build

%install
%make_install

rm -fv %{buildroot}%{_infodir}/dir

%posttrans
echo Note: This emacs is built without process dumping support.
echo This will tack about half a second onto the startup time. If this annoys you,
echo either wait for that to be improved on upstream or run emacs in server mode.

%files
%exclude %{_bindir}/ctags
%exclude %{_mandir}/man1/ctags.1*
%{_bindir}/*
%{_libexecdir}/emacs/%{version}
%{_includedir}/emacs-module.h
%exclude %{_libdir}/systemd
%{_mandir}/man1/*
%{_datadir}/emacs/%{version}
%{_datadir}/emacs/site-lisp
%{_infodir}/*
%exclude %{_datadir}/icons
%exclude %{_datadir}/applications
%exclude %{_datadir}/metainfo

%changelog
