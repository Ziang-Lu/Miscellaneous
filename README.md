# Miscellaneous Topics

This repo contains a variety of topics, including:

## Development Environment Setup

### Bash

* Bash profile file
* For oh-my-zsh installation and configuration, see

  * https://www.zhihu.com/question/20873070/answer/410248435

<br>

### Python Linter Configuration

* `Isort` configuration
  * Check out `.isort.cfg`
* `Pylint` configuration
  * Check out `.pylintrc`
* `Flake8`
  * `Flake8` is a wrapper tool for three tools:
    * `PyFlakes` (static syntax checker)
    * `Pep8` (style checker)
    * `McCabe` (code complexity checker)
  * Check out `flake8` and put it into `~/.config`

<br>

### Text Editor

#### - Vim   (for all)   Configuration

* Check out `.vimrc`
* Follow the instructions to create the directiories and install the corresponding plugins in the comments

#### - Sublime Text 3   (for all)   Preferences & Plugins

* For package control, packages and the corresponding plugins, check out https://www.youtube.com/watch?v=oHmPrjSzmwU
* `Package control`
* `Material Theme`
* `Sidebar Enhancements`
* `SublimeCodeIntel`
* `Anaconda`   (for Python only)
* `BracketHighlighter`
* `SublimeLinter`
* `isort`   (for Python only)
* `SublimeLinter-pylint`   (for Python only)
* `SublimeLinter-flake8`   (for Python only)
* `DocBlockr`
* `GitGutter`

Note that in order to use `subl` command, do the following to create a soft link to that command line tool:

```bash
ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```

#### - Visual Studio Code   (for JavaScript & HTML)   Extensions

* `Material Theme`
* `TODO Highlight`
* `JavaScript (ES6) code snippet`
* `HTML CSS Support`
* `Auto Close Tag`
* `Auto Rename Tag`
* `Live Server`

<br>

### IDE

#### [Java]   IntelliJ Idea Settings

Check out the .jar file

#### [Python]   PyCharm Settings

* For adding `Isort`, `Pylint` and `Flake8` as an external tools, follow similar procedures as https://github.com/timothycrosley/isort/wiki/isort-Plugins

#### [All]   JetBrains Plugins

* CodeGlance
* Presentation Assistant
* IdeaVim
* Checkstyle   *(IntelliJ IDEA)*
* Save Actions
* JSON Viewer

<br>

## Miscellaneous Topics in Coding

### Best Coding Practice

* Java class equality design

### Python Modules

* Python `argparse` module example

### Development-Related

* Logging
* Unit tests

<br>

## License

 This repo is distributed under the <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/LICENSE">MIT license</a>.
