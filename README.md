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
node | ✔ | `node`
python@3.9 | ✔ | `python3.9` (`python`)
postgresql | ✘ |
python@3.8 | ✔✘ | `python3.8`, but no library support yet
imagemagick | ✘ |
youtube-dl | ✘ |
awscli | ✘ |
git | ✘ |
openssl@1.1 | ✔ | `libopenssl`
yarn | ✘ |
ffmpeg | ✘ |
cmake | ✘ |
wget | ✘ |
gnupg | ✔ | `gnupg`
htop | ✘ |
mysql | ✘ |
vim | ✘ |
pyenv | ✘ |
go | ✘ |
automake | ✔ | `automake`
zsh | ✘ |
curl | ✘ |
php | ✘ |
ruby | ✘ |
nvm | ✘ |
tmux | ✘ |
glib | ✔ | `glib2`, `glib2-utils`
ansible | ✘ |
gradle | ✘ |
openjdk | ✘ |
sqlite | ✔ | `libsqlite`, `sqlite`
nginx | ✘ |
coreutils | ✘ |
watchman | ✘ |
redis | ✘ |
libpq | ✘ |
kubernetes-cli | ✘ |
nmap | ✘ |
composer | ✘ |
heroku/brew/heroku | ✘ |
gh | ✘ |
jq | ✘ |
libxml2 | ✘ |
pkg-config | ✔ | `pkgconf` (`pkg-config`)
helm | ✘ |
azure-cli | ✘ |
gcc | ✘ |
telnet | ✘ |
readline | ✔ | `libreadline`
cocoapods | ✘ |
gnutls | ✘ |
krb5 | ✘ |
libtool | ✔ | `libtool` (need to add `glibtool` link)
ruby-build | ✘ |
unbound | ✘ |
maven | ✘ |
terraform | ✘ |
docker | ✘ |
zlib | ✘ |
graphviz | ✘ |
pango | ✘ |
git-lfs | ✘ |
pipenv | ✘ |
minikube | ✘ |
mongodb/brew/mongodb-community | ✘ |
fzf | ✘ |
bash | ✘ |
protobuf | ✘ |
gobject-introspection | ✘ |
libksba | ✔ | `libksba`
pandoc | ✘ |
mysql@5.7 | ✘ |
sphinx-doc | ✔ | `python-sphinx`
gdk-pixbuf | ✘ |
python@3.7 | ✘ |
harfbuzz | ✘ |
rbenv | ✘ |
tree | ✘ |
subversion | ✘ |
libass | ✘ |
aws/tap/aws-sam-cli | ✘ |
php@7.3 | ✘ |
poppler | ✘ |
libyaml | ✔ | `libyaml`
bat | ✘ |
mysql-client | ✘ |
qt | ✘ |
opencv | ✘ |
librsvg | ✘ |
sbt | ✘ |
hugo | ✘ |
unrar | ✘ |
freetds | ✘ |
autoconf | ✔ | `autoconf`
numpy | ✘ |
mercurial | ✘ |
openldap | ✘ |
ccache | ✘ |
fastlane | ✘ |
direnv | ✘ |
