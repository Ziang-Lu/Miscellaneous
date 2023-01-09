# This script will run when a non-login shell is spawned.

alias ll='ls -alh'
alias ..='cd ..'
alias hi='history'
alias free='free -ht'
alias df='df -h'
alias du='du -ha'
alias sed='gsed'
alias curl='curl -L'

# Setting listing colors
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# Setting for coreutils
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"

export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"
export PKG_CONFIG_PATH="/usr/local/opt/openssl@1.1/lib/pkgconfig"

# Setting for openssl
export PATH="/usr/local/opt/openssl/bin:$PATH"

# Setting for Python 3 encoding
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# Setting for Pipenv auto completion
eval "$(pipenv --completion)"

# Setting for VSCode command-line
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"

# Setting for NVM (Node Version Manager)
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"                   # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" # This loads nvm bash_completion

# Setting for Ruby
export PATH="/usr/local/opt/ruby/bin:$PATH"

# Setting for SQLite
export PATH="/usr/local/opt/sqlite/bin:$PATH"

# Setting for MySQL
export PATH="/usr/local/mysql/bin:$PATH"

# Setting for icu4c
export PATH="/usr/local/opt/icu4c/bin:$PATH"
export PATH="/usr/local/opt/icu4c/sbin:$PATH"

# Setting for PostgreSQL
export PATH="/usr/local/opt/postgresql@9.6/bin:$PATH"

# Setting for Redis
export PATH="/usr/local/redis/bin:$PATH"

# Setting for ncurses
export PATH="/usr/local/opt/ncurses/bin:$PATH"

echo 'Hello, Captain!'
