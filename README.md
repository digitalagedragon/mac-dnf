# macdnf

A port of Fedora's [dnf](https://github.com/rpm-software-management/dnf) package
manager to macOS, and a compatible package repository.

Supports both x86_64 and arm64 machines, though some packages (notably `qemu`
and `gcc`) are not yet operational on arm64 due to lack of upstream support.

Since the package repository is small (but getting bigger!) and I am one person
working on this, I'm interested to hear about what people want to use! If you've
decided to try this out (for some reason) and you're missing your favorite
packages from `brew` or whatever, put in an issue and I'll prioritize porting
them.

## Installation

**This conflicts with Homebrew!** I have vague aspirations of changing this, but
`dnf` and `rpm` are set up to assume that packages will be installed in the same
place (here `/usr/local`) everywhere, so modifying them to support
arbitrary-prefix installations is a non-trivial amount of work. I definitely
think it's possible, I just haven't really sat down and hashed out what needs to
change yet.

If you do have Homebrew installed, the following commands _should_ get it out of
the way in a reversible manner:

```
# Unlink all your Homebrew packages
brew list -1 | tee brew_previously_linked.txt | xargs -n 1 brew unlink
# Put them back later (if you want)
<brew_previously_linked.txt xargs -n 1 brew link
```

YMMV, though. I don't use `brew` anywhere at the moment (all my macOS machines
are using `dnf` now) so I haven't tested that.

Then, to install `dnf`:

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

The package repository is currently a work in progress. My current goal is to support most of this sample of Homebrew's top 100 user-installed packages:

## brew100 status

brew pkg | status | dnf pkg
--- | --- | ---
node | ✔ | `node`
python@3.9 | ✔ | `python3.9` (`python`)
postgresql | ✘ |
python@3.8 | ✔✘ | `python3.8`, but no library support yet
imagemagick | ✘ |
youtube-dl | ✘ |
awscli | ✔ | `aws-cli`
git | ✘ |
openssl@1.1 | ✔ | `libopenssl`
yarn | ✘ |
ffmpeg | ✘ |
cmake | ✔ | `cmake`
wget | ✔ | `wget`
gnupg | ✔ | `gnupg`
htop | ✘ |
mysql | ✘ |
vim | ✘ |
pyenv | ✘ |
go | ✘ |
automake | ✔ | `automake`
zsh | ✘ |
curl | ✔ | `curl`, `libcurl`
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
gcc | ✔✘ | Only on `x86_64` hosts.
telnet | ✘ |
readline | ✔ | `libreadline`
cocoapods | ✘ |
gnutls | ✘ |
krb5 | ✔ | `libkrb5`, `krb5`
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
qt | ✔ | `libqt`
opencv | ✘ |
librsvg | ✘ |
sbt | ✘ |
hugo | ✘ |
unrar | ✘ |
freetds | ✘ |
autoconf | ✔ | `autoconf`
numpy | ✔ | `numpy`
mercurial | ✘ |
openldap | ✘ |
ccache | ✘ |
fastlane | ✘ |
direnv | ✘ |
