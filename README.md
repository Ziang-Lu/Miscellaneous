# Miscellaneous Topics

* My bash profile file
* Git auto-completion script
  * `brew install bash-completion`

  * Copy `git-completion.bash` to the home directory

  * Copy `git-completion.bash` to `/opt/local/etc/bash_completion.d/`

  * Add the following to `~/.bash_profile`:

    ```shell
    if [ -f `brew --prefix`/etc/bash_completion.d/git-completion.bash ]; then
      . `brew --prefix`/etc/bash_completion.d/git-completion.bash
    fi
    ```
* My vim configuration
  * Follow the instructions to create the directiories and install the corresponding plugins in the comments
* My IDE settings
* Logging
* Unit tests

