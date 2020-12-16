# macdnf

A port of Fedora's [dnf](https://github.com/rpm-software-management/dnf) package manager to macOS, and a (currently small) package repository.
Supports both x86_64 and arm64 machines.

## Installation

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/digitalagedragon/mac-dnf/main/install.sh)"
```

Or clone this repo and run `install.sh` directly.

## Uninstallation

```
rpm -qa | xargs rpm -e
```

## Notes

This is still in very early development. The author has tested it somewhat on a few Big Sur (both architectures) machines, but there's no guarantee it won't make demons fly out of your nose. Pull requests / issues welcome.

The package repository is currently tiny. I'm currently working on porting Homebrew's top 100 packages, but until that gets done you really can't install much beyond `dnf` itself.
