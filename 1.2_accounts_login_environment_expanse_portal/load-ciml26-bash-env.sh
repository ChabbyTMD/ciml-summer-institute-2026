#!/usr/bin/env bash
#
# Load .bashrc.ciml26 and .bash_profile.ciml26 environment.

cp .bashrc "${HOME}"
cp .bash_profile "${HOME}"

cp .bashrc.md5 "${HOME}"
cp .bash_profile.md5 "${HOME}"

cd "${HOME}"

md5sum -c .bashrc.md5
md5sum -c .bash_profile.md5

source .bash_profile
