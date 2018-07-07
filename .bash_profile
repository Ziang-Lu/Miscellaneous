# TODO: understand shell script

# Setting prompt text & color
export PS1="\e[0;32m [Captain \w] \$ \[\e[0m\]"

alias ll="ls -al"
alias hi="history"
alias vi="vim"
alias shuf="gshuf"

# Setting listing colors
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# Setting for Python 3 encoding
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# Setting PATH for Python 3.5
PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH

# Setting PATH for Python 3.6
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

# Setting PATH for Python 3.6.5
# TODO: add this

# Setting PATH for Android
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/platform-tools 

# Setting Git auto-completion
source ~/git-completion.bash

