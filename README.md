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

For Python auto-formatters like `Yapf`, check out https://github.com/google/yapf; but in my text editor and IDEs, I didn't configure any Python auto-formatter.

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

Note that in order to use `subl` command, do the following to create a soft link to that command-line tool:

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

#### [Java]   IntelliJ IDEA Settings

Check out the .jar file

#### [Python]   PyCharm Settings

* For adding `Isort` and `Flake8` as an external tools, follow similar procedures as https://github.com/timothycrosley/isort/wiki/isort-Plugins

#### [All]   JetBrains Plugins

* `CodeGlance`

* `Presentation Assistant`

* `IdeaVim`

* `Checkstyle`   *(IntelliJ IDEA)*

* `Pylint`   *(PyCharm)*

  * In Preference -> Other Settings -> Pylint, set

    Path to Pylint executable: `/usr/local/bin/pylint`

    Path to pylintrc: `/Users/Ziang_Lu/.pylintrc`

* `JSON Viewer`

<br>

## MySQL Server Configuration

Put the `my.cnf` file under `/etc` folder

<br>

## Miscellaneous Topics in Coding

### Java-Related Knowledges

* <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Java-Related/Java%20Reference%20Types.md">Java reference types</a>
* <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Java-Related/LinkedHashMap">LinkedHashMap</a>

### Python-Related

* Knowledge
  
  * <a href="https://github.com/Ziang-Lu/Miscellaneous/tree/master/Python-Related/Knowledge/Metaclass">Metaclass</a>
* Python Standard Library
  
  * <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Python%20Standard%20Modules%20Demo/argparse_demo.py">Python `argparse` module example</a>
  
  * <a href="[https://github.com/Ziang-Lu/Miscellaneous/tree/master/Python-Related/Python%20Standard%20Library/collections-OrderedDict](https://github.com/Ziang-Lu/Miscellaneous/tree/master/Python-Related/Python Standard Library/collections-OrderedDict)">`collections`-`OrderedDict`</a>
  
    This is very similar to `LinkedHashMap` in `Java`.

### Development-Related

|        | Logging                                                      | Unit tests                                                   | Code coverage (by test cases)                                | Profling                                                     |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Java   |                                                              | <a href="https://github.com/Ziang-Lu/Miscellaneous/tree/master/Unit%20Tests/JUnit%20for%20Java">`JUnit`</a> |                                                              |                                                              |
| Python | <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Logging/err.py">`logging`</a> | <a href="[https://github.com/Ziang-Lu/Miscellaneous/tree/master/Unit%20Tests/unittest%20for%20Python](https://github.com/Ziang-Lu/Miscellaneous/tree/master/Unit Tests/unittest for Python)">`unittest`</a><br>`pytest` | <a href="[https://github.com/Ziang-Lu/Miscellaneous/blob/master/Code%20Coverage/Python/Python%20Code%20Coverage.md](https://github.com/Ziang-Lu/Miscellaneous/blob/master/Code Coverage/Python/Python Code Coverage.md)">Overview</a><br>`coverage`<br>`pytest-cov` | <a href="[https://github.com/Ziang-Lu/Miscellaneous/blob/master/Profiling/Python%20Profiling.md](https://github.com/Ziang-Lu/Miscellaneous/blob/master/Profiling/Python Profiling.md)">Overview</a><br>`time`<br>`timeit`<br>`cProfile` (+ `snakeviz`)<br>`line_profiler`<br>`yappi` |
## License

 This repo is distributed under the <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/LICENSE">MIT license</a>.

