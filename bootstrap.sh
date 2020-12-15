#!/usr/bin/env bash

set -e
set -x

cd $(dirname $0)

FILE_VERSION=5.39
LIBARCHIVE_VERSION=3.4.3
LIBGCRYPT_VERSION=1.8.7
LIBGPG_ERROR_VERSION=1.39
LUA_VERSION=5.4.2
PKGCONF_VERSION=1.7.3
POPT_VERSION=1.18
RPM_VERSION=4.16.1
SQLITE_VERSION=3.34.0

mkdir -p bootstrap
cd bootstrap

mkdir -p prefix
PREFIX=$PWD/prefix

OLDPATH=$PATH
export PATH=$PWD/prefix/bin:$PATH
export PKG_CONFIG=$PWD/prefix/bin/pkgconf
export PKG_CONFIG_PATH=$PWD/prefix/lib/pkgconfig
export CPPFLAGS=-I$PWD/prefix/include
export LDFLAGS=-L$PWD/prefix/lib

SQLITE_REAL_VERSION=$(echo $SQLITE_VERSION | perl -nE '@v=split /\./;$v[3]//=0;print shift@v;say map{sprintf("%02d",$_)}@v;')

echo "Downloading sources..."
[ -e file-${FILE_VERSION}.tar.gz ] || curl -LO ftp://ftp.astron.com/pub/file/file-${FILE_VERSION}.tar.gz
[ -e libarchive-${LIBARCHIVE_VERSION}.tar.gz ] || curl -LO https://www.libarchive.org/downloads/libarchive-${LIBARCHIVE_VERSION}.tar.gz
[ -e libgcrypt-${LIBGCRYPT_VERSION}.tar.bz2 ] || curl -LO https://gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-${LIBGCRYPT_VERSION}.tar.bz2
[ -e libgpg-error-${LIBGPG_ERROR_VERSION}.tar.bz2 ] || curl -LO https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-${LIBGPG_ERROR_VERSION}.tar.bz2
[ -e lua-${LUA_VERSION}.tar.gz ] || curl -LO https://www.lua.org/ftp/lua-${LUA_VERSION}.tar.gz
[ -e pkgconf-${PKGCONF_VERSION}.tar.gz ] || curl -LO https://distfiles.dereferenced.org/pkgconf/pkgconf-${PKGCONF_VERSION}.tar.gz
[ -e popt-${POPT_VERSION}.tar.gz ] || curl -LO http://ftp.rpm.org/popt/releases/popt-${POPT_VERSION%.*}.x/popt-${POPT_VERSION}.tar.gz
[ -e rpm-${RPM_VERSION}.tar.bz2 ] || curl -LO http://ftp.rpm.org/releases/rpm-${RPM_VERSION%.*}.x/rpm-${RPM_VERSION}.tar.bz2
[ -e sqlite-autoconf-${SQLITE_REAL_VERSION}.tar.gz ] || curl -LO https://sqlite.org/2020/sqlite-autoconf-${SQLITE_REAL_VERSION}.tar.gz

echo "Extracting sources..."
[ -e file-${FILE_VERSION} ] || tar xf file-${FILE_VERSION}.tar.gz
[ -e libarchive-${LIBARCHIVE_VERSION} ] || tar xf libarchive-${LIBARCHIVE_VERSION}.tar.gz
[ -e libgcrypt-${LIBGCRYPT_VERSION} ] || tar xf libgcrypt-${LIBGCRYPT_VERSION}.tar.bz2
[ -e libgpg-error-${LIBGPG_ERROR_VERSION} ] || tar xf libgpg-error-${LIBGPG_ERROR_VERSION}.tar.bz2
[ -e lua-${LUA_VERSION} ] || tar xf lua-${LUA_VERSION}.tar.gz
[ -e pkgconf-${PKGCONF_VERSION} ] || tar xf pkgconf-${PKGCONF_VERSION}.tar.gz
[ -e popt-${POPT_VERSION} ] || tar xf popt-${POPT_VERSION}.tar.gz
[ -e sqlite-autoconf-${SQLITE_REAL_VERSION} ] || tar xf sqlite-autoconf-${SQLITE_REAL_VERSION}.tar.gz
[ -e rpm-${RPM_VERSION} ] || {
    tar xf rpm-${RPM_VERSION}.tar.bz2
    cd rpm-${RPM_VERSION}
    for patch in $(ls ../../rpmbuild/SOURCES/rpm-*.patch); do
        patch -Np0 <$patch
    done
    cd ..
}

echo "Building pkgconf ${PKGCONF_VERSION}..."
cd pkgconf-${PKGCONF_VERSION}
[ -e Makefile ] || ./configure --prefix=$PREFIX
make -j$(sysctl -n hw.ncpu)
make install
cd ..

echo "Building file ${FILE_VERSION}..."
cd file-${FILE_VERSION}
[ -e Makefile ] || ./configure --prefix=$PREFIX
make -j$(sysctl -n hw.ncpu)
make install
cd ..

echo "Building libgpg-error ${LIBGPG_ERROR_VERSION}..."
cd libgpg-error-${LIBGPG_ERROR_VERSION}
[ -e Makefile ] || ./configure --prefix=$PREFIX
make -j$(sysctl -n hw.ncpu)
make install
cd ..

echo "Building libgcrypt ${LIBGCRYPT_VERSION}..."
cd libgcrypt-${LIBGCRYPT_VERSION}
[ -e Makefile ] || ./configure --prefix=$PREFIX
[ -e src/libgcrypt-config ] || make -j$(sysctl -n hw.ncpu)
[ -e $PREFIX/bin/libgcrypt-config ] || make install
cd ..

echo "Building popt ${POPT_VERSION}..."
cd popt-${POPT_VERSION}
[ -e Makefile ] || ./configure --prefix=$PREFIX
make -j$(sysctl -n hw.ncpu)
make install
cd ..

echo "Building libarchive ${LIBARCHIVE_VERSION}..."
cd libarchive-${LIBARCHIVE_VERSION}
[ -e Makefile ] || ./configure --prefix=$PREFIX
make -j$(sysctl -n hw.ncpu)
make install
cd ..

echo "Building SQLite ${SQLITE_VERSION}..."
cd sqlite-autoconf-${SQLITE_REAL_VERSION}
[ -e Makefile ] || ./configure --prefix=$PREFIX
make -j$(sysctl -n hw.ncpu)
make install
cd ..

echo "Building lua ${LUA_VERSION}..."
cd lua-${LUA_VERSION}
sed -e "s|INSTALL_TOP=.*|INSTALL_TOP= $PREFIX|" -Iold Makefile
make -j$(sysctl -n hw.ncpu)
make install
cat > $PREFIX/lib/pkgconfig/lua.pc <<EOF
V=${LUA_VERSION%.*}
R=${LUA_VERSION}

prefix=$PREFIX
INSTALL_BIN=\${prefix}/bin
INSTALL_INC=\${prefix}/include
INSTALL_LIB=\${prefix}/lib
INSTALL_MAN=\${prefix}/share/man/man1
INSTALL_LMOD=\${prefix}/share/lua/\${V}
INSTALL_CMOD=\${prefix}/lib/lua/\${V}
exec_prefix=\${prefix}
libdir=\${exec_prefix}/lib
includedir=\${prefix}/include

Name: Lua
Description: An Extensible Extension Language
Version: \${R}
Requires:
Libs: -L\${libdir} -llua -lm -ldl
Cflags: -I\${includedir}
EOF

cd ..

echo "Building RPM ${RPM_VERSION}..."

cd rpm-${RPM_VERSION}
[ -e Makefile ] || ./configure --prefix=$PREFIX \
    --disable-bdb --enable-sqlite \
    CFLAGS="-Wno-implicit-function-declaration -Wno-unused-function"
[ -e rpm ] || make -j$(sysctl -n hw.ncpu)
[ -e $PREFIX/bin/rpm ] || make install
cd ..

cat >$PREFIX/lib/rpm/macros.d/macros.bootstrap <<EOF
%_db_backend sqlite
%_topdir ${PREFIX}/../../rpmbuild
%_srcrpmdir %{_topdir}/../bootstrap/SRPMS
%_rpmdir %{_topdir}/../bootstrap/RPMS
%_usr /usr/local/
EOF

cp ../rpmbuild/SOURCES/rpm-1000-macros.src $PREFIX/lib/rpm/macros.d/macros.macdnf

echo '%_prefix /usr/local' >>$PREFIX/lib/rpm/platform/$(uname -m | sed -e 's/arm64/aarch64/')-$(uname -s | tr '[:upper:]' '[:lower:]')/macros

sed -e "s|^/usr|$PREFIX|" -Iold $PREFIX/lib/rpm/find-provides
sed -e "s|^/usr|$PREFIX|" -Iold $PREFIX/lib/rpm/find-requires
rm -f $PREFIX/lib/rpm/perl.req

PACKAGES="apple-perl apple-bsdutils gettext autoconf automake"
PACKAGES="$PACKAGES libtool pkgconf file libgpg-error libgcrypt"
PACKAGES="$PACKAGES libpopt libarchive libsqlite lua python xz libpcre rpm"

for pkg in $PACKAGES; do
    $PREFIX/bin/rpm -q $pkg || {
        $PREFIX/bin/rpmbuild -ba ../rpmbuild/SPECS/$pkg.spec
        PKGS=""
        for subpkg in $($PREFIX/bin/rpmspec -q ../rpmbuild/SPECS/$pkg.spec); do
            PKGS="$PKGS $(echo RPMS/**/$subpkg.rpm)"
        done
        $PREFIX/bin/rpm -i $PKGS
    }
done


export PATH=$OLDPATH
unset PKG_CONFIG
unset PKG_CONFIG_PATH
unset CPPFLAGS
unset LDFLAGS

REBUILD_PKGS="$PACKAGES"

pushd ../rpmbuild
echo "_topdir $PWD" >~/.rpmmacros
popd

# now start building with installed rpm
# important because bootstrap rpm doesn't have working xz
PACKAGES="cmake libsolv setuptools meson asciidoc ninja-build"
PACKAGES="$PACKAGES libffi gettext glib2 util-linux apple-awk libcheck libopenssl"
PACKAGES="$PACKAGES curl libassuan libksba libnpth gnupg swig libgpgme"
PACKAGES="$PACKAGES libxml2 libargp libzstd libzchunk librepo libcppunit libjson-c"
PACKAGES="$PACKAGES python-sphinx libyaml libmodulemd libdnf libcomps dnf"
PACKAGES="$PACKAGES createrepo_c system-release"

for pkg in $PACKAGES; do
    /usr/local/bin/rpm -q $pkg || {
        /usr/local/bin/rpmbuild -ba ../rpmbuild/SPECS/$pkg.spec
        PKGS=""
        for subpkg in $(/usr/local/bin/rpmspec -q ../rpmbuild/SPECS/$pkg.spec); do
            PKGS="$PKGS $(echo ../rpmbuild/RPMS/**/$subpkg.rpm)"
        done
        /usr/local/bin/rpm -i $PKGS
    }
done

for pkg in $REBUILD_PKGS; do
    echo $pkg
    [ -e ../rpmbuild/SRPMS/"$(/usr/local/bin/rpmspec -q --srpm ../rpmbuild/SPECS/$pkg.spec | sed -E 's|\.[^.]*$||')".src.rpm ] \
        || /usr/local/bin/rpmbuild -ba ../rpmbuild/SPECS/$pkg.spec
done

cat > /usr/local/etc/yum.repos.d/local.repo <<EOF
[local]
name=local
baseurl=file:///Users/morgan/src/rpm/repo
enabled=1
metadata_expire=1d
gpgcheck=0
EOF

cd ..
mkdir -p repo
cd repo
rm -r *
cp -r ../rpmbuild/RPMS/* .
createrepo_c .
dnf makecache

rpm -qa | xargs dnf mark remove
dnf mark install dnf
dnf mark install system-release
dnf autoremove
