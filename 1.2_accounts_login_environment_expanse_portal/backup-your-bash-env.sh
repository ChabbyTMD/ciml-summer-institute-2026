#!/usr/bin/env bash
#
# Create a backup of your .bashrc and .bash_profile files

cd "${HOME}"

cp -p .bashrc .bashrc.bak
cp -p .bash_profile .bash_profile.bak

chmod u-w .bashrc.bak
chmod u-w .bash_profile.bak

md5sum .bashrc.bak > .bashrc.bak.md5
md5sum .bash_profile.bak > .bash_profile.bak.md5

chmod u-w .bashrc.bak.md5
chmod u-w .bash_profile.bak.md5
