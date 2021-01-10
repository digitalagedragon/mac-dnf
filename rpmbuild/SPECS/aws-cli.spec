%define system_python 3.9

Name:           aws-cli
Version:        2.1.17
Release:        1%{?dist}
Summary:        Official AWS command-line interface

License:        Apache-2.0
URL:            https://aws.amazon.com/cli/
%undefine       _disable_source_fetch
Source0:        https://github.com/aws/aws-cli/archive/%{version}.tar.gz#/aws-cli-%{version}.tar.gz
%define         SHA256SUM0 67bf406208ea47cb6f3ed6b21533bde01cc5cfc35dce6b1214fabbff9dd5e662

# X10-Update-Spec: { "type": "git-tags",
# X10-Update-Spec:   "repo": "https://github.com/aws/aws-cli.git",
# X10-Update-Spec:   "pattern": "^v(\\d+\\.\\d+\\.\\d+)$" }

BuildRequires:  setuptools
BuildRequires:  pkgconfig(python-%{system_python})
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(openssl)

Requires:       setuptools

%description

%prep
echo "%SHA256SUM0  %SOURCE0" | shasum -a256 -c -
%autosetup

%build

%install
python3 -m pip install --root %{buildroot} --prefix %{_prefix} -r requirements.txt .

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -fv %{buildroot}%{_infodir}/dir
