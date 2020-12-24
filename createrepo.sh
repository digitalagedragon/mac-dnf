cd $(dirname $0)
cd repo
rm -rf *
cp -r ../rpmbuild/RPMS/* .
createrepo_c .
dnf makecache --repo local
