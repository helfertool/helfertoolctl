#!/bin/bash

set -e

# base directory
basedir="$(dirname "$(dirname "$(readlink -f "$0")")")"
cd "$basedir/src"

# debian
if [ "$1" == "debian" ] ; then
    debuild -us -uc
else
    echo "Commands: debian"
    exit 1
fi
