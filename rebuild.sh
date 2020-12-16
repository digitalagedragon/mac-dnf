#!/usr/bin/env bash

set -e
set -x

XID=$(dnf history info | head -n1 | cut -d ':' -f 2)
trap dnf history rollback -y $XID EXIT
SPEC=$1

BUILDREQUIRES=$(rpmspec -q --buildrequires $SPEC)
[ -n "$BUILDREQUIRES" ] && dnf install -y $BUILDREQUIRES
rpmbuild -ba $@
