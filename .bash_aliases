alias ll='ls -alh'
alias ..='cd ..'
alias hi='history'

alias clear_pyc='find ./ -name "*.pyc" -exec rm {} \;'

# File operations
alias cat='cat -n'  # with line numbers
alias less='less -n'  # with line numbers
alias tail='tail -f'  # keeps refreshing (can be used to monitor a ever-growing log file)
alias grep='grep -i -n'  # ignoring cases & with line numbers
alias sed='gsed'

# System monitoring
alias free='free -ht'
alias df='df -h'
alias du='du -ha'

# Networking
alias curl='curl -L'