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

### JavaScript / TypeScript Linter Configuration

`ESLint` is responsible for checking syntax errors and problems, while `Prettier` for auto-formatting our JavaScript codes.

Check out https://github.com/Ziang-Lu/JavaScript-Learning-Notes#javascript-linting and https://github.com/Ziang-Lu/JavaScript-Learning-Notes/blob/master/TypeScript-crash-course/TypeScript%20Learning%20Notes.md#typescript-linting

<br>

### Text Editor

#### - Vim   (for all)   Configuration

* Check out `.vimrc`
* Follow the instructions to create the directiories and install the corresponding plugins in the comments

#### - Sublime Text 3 Preferences & Plugins

For package control, packages and the corresponding plugins, check out https://www.youtube.com/watch?v=oHmPrjSzmwU

* `Package control`
* `Material Theme`
* `Sidebar Enhancements`
* `SublimeCodeIntel`
* `BracketHighlighter`
* `SublimeLinter`
* `DocBlockr`
* `GitGutter`

Python:
* `Anaconda`
* `isort`
* `SublimeLinter-pylint`
* `SublimeLinter-flake8`

Dev & Ops
* `nginx`
* `Dockerfile Syntax Highlighting`

Note that in order to use `subl` command, do the following to create a soft link to that command-line tool:

```bash
ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```

#### - VSCode Extensions

* `Material Theme`
* `TODO Highlight`
* `Rainbow Brackets`
* `Prettify JSON`
* `GitLens`

C/C++
* `C/C++ (by Microsoft)`

* `Header Source Switch`

* `cpplint`

  ```bash
  $ sudo pip3 install cpplint
  ```

* `clang-format`

  ```bash
  $ brew install clang-format
  ```

* `CodeLLDB`

JavaScript / TypeScript
* `JavaScript (ES6) code snippet`
* `ESLint`
* `Prettier`

HTML & CSS
* `HTML CSS Support`
* `Auto Close Tag`
* `Auto Rename Tag`
* `Highlight Matching Tag`

Web Development
* `Live Server`

Dev & Ops
* `Docker`

<br>

### IDE (JetBrains Plugins)

* `Material Theme UI`

* `Shell Script`

* `CodeGlance`

* `IdeaVim` (disabled)

* `Git Flow Integration`

* `Grep Console`

* `Presentation Assistant`

* `Checkstyle`   *(IntelliJ IDEA)*

* `Alibaba Java Coding Guidelines`   *(IntelliJ IDEA)*

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

### General Knowledges

* <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B/%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B.md">网络编程 (via socket)</a>

### Java-Related Knowledges

* <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Java-Related/Java%20Reference%20Types.md">Java reference types</a>
* <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Java-Related/LinkedHashMap">LinkedHashMap</a>

### Python-Related

* Knowledge
  
  * <a href="https://github.com/Ziang-Lu/Miscellaneous/tree/master/Python-Related/Knowledge/Metaclass">Metaclass</a>
* Python Standard Library
  
  * <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Python%20Standard%20Modules%20Demo/argparse_demo.py">Python `argparse` module example</a>
  
  * <a href="https://github.com/Ziang-Lu/Miscellaneous/tree/master/Python-Related/Python Standard Library/collections-OrderedDict">`collections`-`OrderedDict`</a>
  
    This is very similar to `LinkedHashMap` in `Java`.

* Static Type-Checking
  
  * <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Python-Related/Static%20Type-Checking.md">`typing` auxiliary examples</a>

<br>

## License

 This repo is distributed under the <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/LICENSE">MIT license</a>.

