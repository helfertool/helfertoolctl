# Dependencies for build

To build the packages on Debian, the following packages need to be installed:

 * devscripts

# Shared files with helfertool repository

Some files are usually managed in the helfertool repository, but also part of this repo:

* src/config/helfertool.yaml (slightly modified for Docker)
* src/share/unavailable.html

# Release new version

## Set environment variables

Set environment (in case it is not stored in config files, for example in devcontainer):

    export DEBEMAIL="hertle@narfi.net"
    export DEBFULLNAME="Sven Hertle"

## Bump version

Bump version, run in `src`:

```
dch -i
```

The version is also used for the CentOS package.

## Debian

Build and sign the Debian packages:

```
./scripts/build.sh debian
debsign -k E2CB30B56CCCF2027CE115A1FA1023F9F6AC494F helfertoolctl_0.9.2.dsc
```

Add packages to Debian repo with reprepro:

```
reprepro includedeb unstable ~/helfertoolctl_X.Y.Z_amd64.deb
reprepro includedsc unstable ~/helfertoolctl_X.Y.Z.dsc
```

After testing, move to buster and bullseye repository:

```
reprepro copy bullseye unstable helfertoolctl
reprepro copy bookworm unstable helfertoolctl
```

## CentOS

Build the CentOS packages:

```
./scripts/build.sh centos
```

Copy packages to `centos/7/x86_64/testing` directory, remove old version and run:

```
createrepo_c .
gpg --detach-sign --armor repodata/repomd.xml
```

After testing, copy package from `testing` to `stable` and run commands again.

## Git tag

Add a git tag for the released version:

    git tag -a v0.1.19 -m "version 0.1.19"
    git push origin --tags

# LICENSE

Copyright (C) 2018-2022  Sven Hertle and contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
