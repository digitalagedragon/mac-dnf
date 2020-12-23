set -e

cd $(dirname $0)

spec=$1

for source in $(rpmspec -P ../rpmbuild/SPECS/$spec 2>/dev/null | egrep 'Source[[:digit:]]+:[[:space:]]*[^[:space:]]+://' | awk '{print $2}'); do
    if [[ -n $source ]]; then
        curl -s -L -f $source > /tmp/$(basename $source)
        oldpwd=$(pwd)
        cd /tmp
        shasum -a256 $(basename $source)
        rm $(basename $source)
        cd $oldpwd
    fi
done