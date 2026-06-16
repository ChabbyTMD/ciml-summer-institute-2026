#!/usr/bin/env bash
#
# Create a backup of your .bashrc and .bash_profile files

cd "${HOME}"

cp -p .bashrc .bashrc.bak
cp -p .bash_profile .bash_profile.bak

chmod u-w .bashrc.bak
chmod u-w .bash_profile.bak
