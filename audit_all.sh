#!/usr/bin/env bash

set -e

cd $(dirname $0)

for pkg in $(cat packages.order); do
    if [[ $pkg = *":"* ]]; then
        # architecture-specific package
        arch=${pkg%:*}
        pkg=${pkg#*:}
    else
        arch=""
    fi
    if [[ -z $arch ]] || [[ $arch = $(uname -m) ]]; then
        perl maint-tools/audit.pl rpmbuild/SPECS/$pkg.spec
    fi
done
