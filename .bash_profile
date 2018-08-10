# This script is run when a login shell is spawned.

# Simple call .bashrc
if [ -f ~/.bashrc]; then
    source ~/.bash_profile
fi
