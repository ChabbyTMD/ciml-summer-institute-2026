#!/usr/bin/env bash
#
# Create a backup of your .bashrc and .bash_profile files

cd "${HOME}"

cp .bashrc .bashrc.bak
cp .bash_profile .bash_profile.bak

chmod u-w .bashrc.bak
chmod u-w .bash_profile.bak
