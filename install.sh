#!/usr/bin/env bash

cd $(dirname $0)

echo "### Setting up /usr/local... (requires sudo)"
echo "This will create a directory structure under /usr/local and reassign its ownership."
echo "If you have Homebrew installed, this is a good time to kill the script and move or uninstall it."

my_uid=$(id -u)
my_gid=$(id -g)

sudo mkdir -p /usr/local/{bin,etc,include,lib,libexec,opt,sbin,share,var}
sudo chown $my_uid:$my_gid /usr/local/{bin,etc,include,lib,libexec,opt,sbin,share,var}

echo "### Downloading bootstrap packages..."
cd /tmp
curl -LO http://digitalis-repository.s3-website-us-west-1.amazonaws.com/macdnf/preinstall-$(uname -m).tar.gz

echo "### Unpacking bootstrap packages..."
cd /usr/local
tar xzf /tmp/preinstall-$(uname -m).tar.gz bin etc include lib share var
rm /tmp/preinstall-$(uname -m).tar.gz

echo "### Reinstalling from DNF repository..."
dnf install -y dnf system-release repository
