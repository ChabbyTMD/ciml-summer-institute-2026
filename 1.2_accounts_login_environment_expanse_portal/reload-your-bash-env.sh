#!/usr/bin/env bash
#
# Reload your .bashrc and .bash_profile files from *.bak

cd "${HOME}"

cp .bashrc.bak .bashrc
cp .bash_profile.bak .bash_profile

chmod u+w .bashrc
chmod u+w .bash_profile

cp -f .bashrc.bak.md5 .bashrc.md5
cp -f .bash_profile.bak.md5 .bash_profile.md5

md5sum -c .bashrc.md5
md5sum -c .bash_profile.md5
