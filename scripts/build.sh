#!/bin/bash

set -e

# base directory
basedir="$(dirname "$(dirname "$(readlink -f "$0")")")"
cd "$basedir/src"

# debian
if [ "$1" == "debian" ] ; then
    debuild -us -uc
# centos
elif [ "$1" == "centos" ] ; then
    # create archive with source code and copy it to rpmbuild directory
    mkdir -p "$HOME/rpmbuild/SOURCES"
    tar cf "$HOME/rpmbuild/SOURCES/helfertoolctl.tar" helfertoolctl

    # build rpm
    rpmbuild -ba helfertoolctl.spec

    # get rpm and cleanup
    rpmfile="$(ls "$HOME/rpmbuild/RPMS/x86_64/")"
    cp "$HOME/rpmbuild/RPMS/x86_64/$rpmfile" ..
    rm -rf "$HOME/rpmbuild/"

    # sign file
    rpm --addsign "../$rpmfile"
else
    echo "Commands: debian, centos"
    exit 1
fi
