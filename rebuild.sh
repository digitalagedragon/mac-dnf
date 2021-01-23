#!/usr/bin/env bash

set -e
set -x

XID=$(dnf history info | head -n1 | cut -d ':' -f 2)
trap "dnf history rollback -qy $XID" EXIT

rpm -qa | xargs dnf mark -q remove
dnf mark -q install dnf repository system-release createrepo_c
dnf autoremove -qy

SPEC=$1
shift

BUILDREQUIRES=$(rpmspec -q --buildrequires $SPEC $@)
[ -n "$BUILDREQUIRES" ] && dnf install -y  $BUILDREQUIRES
rpmbuild -ba $SPEC $@
sh createrepo.sh
perl maint-tools/audit.pl $SPEC || {
    rm rpmbuild/SRPMS/"$(/usr/local/bin/rpmspec -q --srpm $SPEC | sed -E 's|\.[^.]*$||')".src.rpm
    false
}
