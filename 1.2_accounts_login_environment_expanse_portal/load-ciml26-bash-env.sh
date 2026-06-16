#!/usr/bin/env bash
#
# Load CIML26 .bashrc and .bash_profile into your environment.

cp .bashrc "${HOME}"
cp .bash_profile "${HOME}"

cp .bashrc.md5 "${HOME}"
cp .bash_profile.md5 "${HOME}"

cd "${HOME}"

chmod u-w .bashrc.md5
chmod u-w .bash_profile.md5

md5sum -c .bashrc.md5
md5sum -c .bash_profile.md5
