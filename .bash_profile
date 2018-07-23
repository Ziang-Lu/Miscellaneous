# TODO: understand shell script

# Setting Git branch display
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# Setting prompt text & color
export PS1="\e[0;32m [Captain \w] $(parse_git_branch) \$ \[\e[0m\]"

alias ll="ls -al"
alias hi="history"
alias vi="vim"
alias shuf="gshuf"
# Hard-code for pip installation location
alias pip="/usr/local/bin/pip"

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
if [ -f `brew --prefix`/etc/bash_completion.d/git-completion.bash ]; then
  . `brew --prefix`/etc/bash_completion.d/git-completion.bash
fi

# Setting for Node Version Manager (NVM)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# Settings for SportDex Cocoapods
export PATH="/usr/local/opt/icu4c/bin:$PATH"
export PATH="/usr/local/opt/icu4c/sbin:$PATH"

