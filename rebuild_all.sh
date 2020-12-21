#!/usr/bin/env bash

set -e
set -x

cd $(dirname $0)

for pkg in $(cat packages.order); do
    [ -e rpmbuild/SRPMS/"$(/usr/local/bin/rpmspec -q --srpm rpmbuild/SPECS/$pkg.spec | sed -E 's|\.[^.]*$||')".src.rpm ] \
        || {
            ./rebuild.sh rpmbuild/SPECS/$pkg.spec
            cd repo
            rm -rf *
            cp -r ../rpmbuild/RPMS/* .
            createrepo_c .
            dnf makecache --repo local
            cd ..
        }
done

if [ $(uname -m) = "arm64" ]; then
    for pkg in $(cat packages.universal); do
        [ -e rpmbuild/SRPMS/"$(/usr/local/bin/rpmspec -q --srpm rpmbuild/SPECS/$pkg.spec --with universal | sed -E 's|\.[^.]*$||')".src.rpm ] \
            || {
                ./rebuild.sh rpmbuild/SPECS/$pkg.spec --with universal
                cd repo
                rm -rf *
                cp -r ../rpmbuild/RPMS/* .
                createrepo_c .
                dnf makecache --repo local
                cd ..
            }
    done
fi