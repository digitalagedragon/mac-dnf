# macdnf

A port of Fedora's [dnf](https://github.com/rpm-software-management/dnf) package manager to macOS, and a (currently small) package repository.
Supports both x86_64 and arm64 machines.

## Installation

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/digitalagedragon/mac-dnf/main/install.sh)"
```

Or clone this repo and run `install.sh` directly.

## Uninstallation

```
rpm -qa | xargs rpm -e
```

## Notes

This is still in very early development. The author has tested it somewhat on a few Big Sur (both architectures) machines, but there's no guarantee it won't make demons fly out of your nose. Pull requests / issues welcome.

The package repository is currently tiny. I'm currently working on porting Homebrew's top 100 packages, but until that gets done you really can't install much beyond `dnf` itself.


## brew100 status

brew pkg | status | dnf pkg
--- | --- | ---
python@3.9 | ✔ | `python3.9`
openssl@1.1 | ✔ | `libopenssl`
sqlite | ✔ | `libsqlite`, `sqlite`
readline | ✘
node | ✘
gmp | ✘
gdbm | ✘
icu4c | ✘ | `libicu4c`, in progress
libtiff | ✘
gettext | ✔ | `gettext`
python@3.8 | ✘
nghttp2 | ✘
unbound | ✘
krb5 | ✘
xz | ✔ | `xz`
glib | ✔ | `glib2`, `glib2-utils`
c-ares | ✘
freetype | ✘
pkg-config | ✔ | `pkgconf` (provides `pkg-config`)
imagemagick | ✘
libtool | ❗ | `libtool`, does not provide `glibtool` yet
postgresql | ✘
pcre2 | ✘ | 
libev | ✘
jemalloc | ✘
pcre | ✔ | `libpcre`, `pcre`
libffi | ✔ | `libffi`
libevent | ✘
libidn2 | ✘
p11-kit | ✘
youtube-dl | ✘
gobject-introspection | ✘
cmake | ✔ | `cmake`
x265 | ✘
libunistring | ✘
gnutls | ✘
git | ✘
awscli | ✘
jpeg | ✘
openjdk | ✘
jansson | ✘
protobuf | ✘
guile | ✘
bdw-gc | ✘
x264 | ✘
ffmpeg | ✘
libpng | ✘
libsndfile | ✘
gnu-getopt | ✘
harfbuzz | ✘
aom | ✘
webp | ✘
pango | ✘
nettle | ✘
fribidi | ✘
oniguruma | ✘
automake | ✔ | `automake`
yarn | ✘
little-cms2 | ✘
freetds | ✘
libass | ✘
pixman | ✔ | `libpixman`
libbluray | ✘
autoconf | ✔ | `autoconf`
libtasn1 | ✘
libpq | ✘
curl | ✘
cairo | ✘
libmpc | ✘
fontconfig | ✘
gnupg | ✔ | `gnupg`
ruby-build | ✘
libyaml | ✔ | `libyaml`
openldap | ✘
libksba | ✔ | `libksba`
graphite2 | ✘
zstd | ✔ | `libzstd`
lz4 | ✘
wget | ✘
go | ✘
gdk-pixbuf | ✘
srt | ✘
lzo | ✘
qt | ✘
ruby | ✘
libde265 | ✘
utf8proc | ✘
rtmpdump | ✘
mysql | ✘
htop | ✘
rubberband | ✘
libomp | ✘
mpfr | ✘
jasper | ✘
ghostscript | ✘
vim | ✘
rav1e | ✘
gcc | ✘
ncurses | ✘
lua | ✔ | `lua`, `liblua`
