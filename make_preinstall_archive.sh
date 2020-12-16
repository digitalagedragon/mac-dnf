#!/usr/bin/env bash

set -e
set -x

cd $(dirname $0)

rm -rf preinstall_root
mkdir preinstall_root
cd preinstall_root

for package in $(cat ../packages.preinstall); do
    RPM=$(rpm -q $package)
    rpm2archive <../rpmbuild/RPMS/**/$RPM.rpm - | tar xz
done

cd ..
tar czpf preinstall-$(uname -m).tar.gz -C preinstall_root/usr/local .