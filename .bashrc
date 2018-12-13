# This script will run when a non-login shell is spawned.

# Setting prompt text & color
PS1="\e[0;32m \n [\u @ \h in \W]\n \$ \[\e[0m\]"
export PS1;

alias ..='cd ..'
alias curl='curl -L'
alias hi='history'
alias ll='ls -al'
alias now='date +"%T"'
alias sed='gsed'
alias shuf='gshuf'
alias vi='vim'

# Setting listing colors
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# Setting for less command with these default options
LESS="-iNs"
# Cause search to ignore case
# Constantly display line numbers
# Display "raw" control characters
# Squeeze consecutive blank lines into one single blank line
export LESS

# Setting for coreutils
export PATH="/usr/local/opt/coreutils/libexec/gnubin:$PATH"

# Setting for openssl
export PATH="/usr/local/opt/openssl/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"

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

# Setting for MySQL
export PATH="/usr/local/mysql/bin:$PATH"

# Setting for Kaggle
export PATH="/Users/Ziang_Lu/Library/Python/3.7/bin:$PATH"

echo 'Hello, Captain!'
