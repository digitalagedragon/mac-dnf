my_uid=$(id -u)
my_gid=$(id -g)

sudo mkdir -p /usr/local/{bin,etc,include,lib,libexec,opt,sbin,share,var}
sudo chown $my_uid:$my_gid /usr/local/{bin,etc,include,lib,libexec,opt,sbin,share,var}
