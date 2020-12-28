#!/usr/bin/env bash

set -e
set -x

XID=$(dnf history info | head -n1 | cut -d ':' -f 2)
trap "dnf history rollback -y $XID" EXIT
SPEC=$1

BUILDREQUIRES=$(rpmspec -q --buildrequires $SPEC $@)
[ -n "$BUILDREQUIRES" ] && dnf install -y --best --allowerasing $BUILDREQUIRES
rpmbuild -ba $@
sh createrepo.sh
perl maint-tools/audit.pl $SPEC || {
    rm rpmbuild/SRPMS/"$(/usr/local/bin/rpmspec -q --srpm rpmbuild/SPECS/$pkg.spec | sed -E 's|\.[^.]*$||')".src.rpm
    false
}
