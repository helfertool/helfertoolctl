# Shared files with helfertool repository

Some files are usually managed in the helfertool repository, but also part of this repo:

* src/config/helfertool.yaml (slightly modified for Docker)
* src/share/unavailable.html

# Release new version

Bump version, run in `src`:

```
dch -i
```

Then build the Debian packages:

```
./scripts/build.sh debian
```

Add packages to Debian repo with reprepro:

```
reprepro includedeb stretch ~/helfertoolctl_X.Y.Z_amd64.deb
reprepro includedsc stretch ~/helfertoolctl_X.Y.Z.dsc
```

# LICENSE

Copyright (C) 2018  Sven Hertle

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
