#!/bin/bash

set -ouex pipefail

### Install packages

# Packages can be installed from any enabled yum repo on the image.
# RPMfusion repos are available by default in ublue main images
# List of rpmfusion packages can be found here:
# https://mirrors.rpmfusion.org/mirrorlist?path=free/fedora/updates/43/x86_64/repoview/index.html&protocol=https&redirect=1

# this installs a package from fedora repos
# dnf5 install -y <package>

# Use a COPR Example:
#
# dnf5 -y copr enable ublue-os/staging
# dnf5 -y install package
# Disable COPRs so they don't end up enabled on the final image:
# dnf5 -y copr disable ublue-os/staging

#### System Unit Files

systemctl enable podman.socket

# bees first-boot setup (discovers root btrfs UUID and enables bees@<UUID>)
cp /ctx/usr/libexec/bees-setup /usr/libexec/bees-setup
cp /ctx/usr/lib/systemd/system/bees-setup.service /usr/lib/systemd/system/bees-setup.service
systemctl enable bees-setup.service
