Name:           repository
Version:        0.1
Release:        1%{?dist}
Summary:        Main dnf repository.
License:        None
BuildArch:      noarch

# X10-Update-Spec: { "type": "none" }

Requires:       dnf

%description
%prep
%build
%install

install -dm755 %{buildroot}/usr/local/etc/yum.repos.d
cat >%{buildroot}/usr/local/etc/yum.repos.d/macdnf.repo <<EOF
[macdnf]
name=macdnf
mirrorlist=http://digitalis-repository.s3-website-us-west-1.amazonaws.com/macdnf/mirrorlist.txt
enabled=1
metadata_expire=1d
# yes i'm going to be signing packages eventually
gpgcheck=0
EOF

%files
/usr/local/etc/yum.repos.d/macdnf.repo

%changelog
