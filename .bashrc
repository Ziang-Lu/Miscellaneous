# This script will run when a non-login shell is spawned.

# Setting prompt text & color
PS1="\e[0;32m \n [\u @ \h in \W]\n \$ \[\e[0m\]"
export PS1;

alias ..='cd ..'
alias ll='ls -al'
alias hi='history'
alias vi='vim'
alias sed='gsed'
alias shuf='gshuf'
alias curl='curl -L'
alias now='date +"%T"'

# Setting listing colors
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# Setting for coreutils
export PATH="usr/local/opt/coreutils/libexec/gnubin:$PATH"

# Setting for Python 3 encoding
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# Setting for NVM (Node Version Manager)
export NVM_DIR="$HOME/.nvm"
. "/usr/local/opt/nvm/nvm.sh"

# Setting for Ruby
export PATH="/usr/local/opt/ruby/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/ruby/lib"
export CPPFLAGS="-I/usr/local/opt/ruby/include"

# Setting for SQLite
export PATH="/usr/local/opt/sqlite/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/sqlite/lib"
export CPPFLAGS="-I/usr/local/opt/sqlite/incldue"

echo 'Hello, Captain!'
