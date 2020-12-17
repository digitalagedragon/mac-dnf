rpm -qa | xargs dnf mark remove
dnf mark install dnf repository system-release createrepo_c
dnf autoremove
