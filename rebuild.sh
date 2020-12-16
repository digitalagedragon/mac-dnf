#!/usr/bin/env bash

set -e
set -x

XID=$(dnf history info | head -n1 | cut -d ':' -f 2)
SPEC=$1

dnf install -y $(rpmspec -q --buildrequires $SPEC)
rpmbuild -ba $@
dnf history rollback -y $XID
