XID=$(dnf history info | head -n1 | cut -d ':' -f 2)

rpm -qa | xargs dnf mark remove
dnf mark install dnf repository system-release createrepo_c
dnf autoremove

echo "dnf history rollback $XID"
