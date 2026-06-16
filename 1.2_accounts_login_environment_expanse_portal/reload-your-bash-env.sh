#!/usr/bin/env bash
#
# Reload your .bashrc and .bash_profile files from *.bak

cd "${HOME}"

cp .bashrc.bak .bashrc
cp .bash_profile.bak .bash_profile

chmod u+w .bashrc
chmod u+w .bash_profile
