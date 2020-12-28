set -e

if [ ! -e "$(dirname $0)/.changelog_uid" ]; then
    echo "Need a .changelog_uid file so I know who you are"
    false
fi

# bump the release number
perl -pe 's/Release:(\s*)(\d+)/"Release:$1" . ($2+1)/e' -i $1
# update the changelog
sh $(dirname $0)/bump_changelog.sh $(basename $1) "$2"
sh rebuild.sh $1
