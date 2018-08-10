# This script will run when a non-login shell is spawned.

# TODO: understand shell script

# Setting prompt text & color
PS1="\e[0;32m \n [\u @ \h in \W]\n \$ \[\e[0m\]"
export PS1;

alias ll="ls -al"
alias hi="history"
alias vi="vim"
alias sed="gsed"
alias shuf="gshuf"

# Setting listing colors
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# Setting for Python 3 encoding
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# Setting for Node Version Manager (NVM)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Setting PATH for Android
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools

# Settings for SportDex Cocoapods
export PATH="/usr/local/opt/icu4c/bin:$PATH"
export PATH="/usr/local/opt/icu4c/sbin:$PATH"
