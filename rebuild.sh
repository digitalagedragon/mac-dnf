#!/usr/bin/env bash

set -e
set -x

XID=$(dnf history info | head -n1 | cut -d ':' -f 2)
SPEC=$1

BUILDREQUIRES=$(rpmspec -q --buildrequires $SPEC)
[ -n "$BUILDREQUIRES" ] && dnf install -y 
rpmbuild -ba $@
dnf history rollback -y $XID
