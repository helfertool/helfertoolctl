Name:           helfertoolctl
Release:        1%{?dist}
Summary:        Install and manage Helfertool with Docker
Packager:       Sven Hertle <hertle@narfi.net>
License:        AGPLv3+
Requires(pre):  shadow-utils

%define version %(grep -E "^helfertoolctl \([0-9\.]*\)" debian/changelog | head -n 1 | grep -Eo '[0-9\.]*')
Version:        %{version}

%description
This package provides an easy way to install the Helfertool with Docker


%prep
rm -rf $RPM_BUILD_DIR/helfertoolctl
tar xf "$RPM_SOURCE_DIR/helfertoolctl.tar"


%install
cd helfertoolctl
make DESTDIR="$RPM_BUILD_ROOT" install

mkdir -p "$RPM_BUILD_ROOT/etc/helfertool/" \
    "$RPM_BUILD_ROOT/etc/default/" \
    "$RPM_BUILD_ROOT/srv/helfertool" \
    "$RPM_BUILD_ROOT/var/log/helfertool"

cp "$RPM_BUILD_DIR/helfertoolctl/config/helfertool.yaml" "$RPM_BUILD_ROOT/etc/helfertool/"
cp "$RPM_BUILD_DIR/helfertoolctl/config/helfertool" "$RPM_BUILD_ROOT/etc/default/"


%files
/usr/sbin/helfertoolctl
/usr/share/helfertool/unavailable.html
/lib/systemd/system/helfertool.service

%config(noreplace) %attr(0640, root, helfertool) /etc/helfertool/helfertool.yaml
%config(noreplace) /etc/default/helfertool

%attr(0770, root, helfertool) /var/log/helfertool
%attr(0770, root, helfertool) /srv/helfertool


%pre
getent group helfertool >/dev/null 2>&1 || groupadd --system helfertool
getent passwd helfertool >/dev/null 2>&1 || useradd --system \
    --home /srv/helfertool \
    --gid helfertool helfertool
