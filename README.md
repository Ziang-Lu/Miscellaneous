# Miscellaneous Topics

This repo contains a variety of topics, including:

## Development Environment Setup

### Command Line Tools & Shell (Bash)

* Some commonly-used commands
* Bash profile file

=> Check out `Dev. & Working Commands.md`

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



#### - VSCode Extensions

https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf

Themes
  * `Material Theme`
  * `Material Icon Theme`
  * `Atom One Dark Theme`
  * `One Dark Pro`

General code highlighting
  * `TODO Highlight`
  * `Prettify JSON`
  * `Rainbow CSV`

`Visual Studio IntelliCode`

C/C++
* `C/C++ (by Microsoft)`
* `cpplint`
  ```bash
  $ sudo pip3 install cpplint
  ```

* `clang-format`
  ```bash
  $ brew install clang-format
  ```


Python
* `Python`

  ```bash
  $ pip3 install autopep8
  ```

* `Pylance`

Bash

* `Bash IDE`
* `shell-format`

Git

  * `GitLens`
  * `Git Graph`

Web Development

* `Live Server`
* RPC - Data transfer (Serialization / Deserialization)
  * `Protobuf support`
  * `Thrift`
* `Thunder Client` for testing RESTful API

JavaScript / TypeScript

* `JavaScript (ES6) code snippet`
* `ESLint`
* `Prettier`

Dev & Ops

* Compiling & building
  * `Bazel`
* Packaging & running & composing
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

  * <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Python-Related/Python%20Standard%20Library/argparse_demo.py">Python `argparse` module example</a>

  * <a href="https://github.com/Ziang-Lu/Miscellaneous/tree/master/Python-Related/Python%20Standard%20Library/collections-OrderedDict">`collections`-`OrderedDict`</a>

    This is very similar to `LinkedHashMap` in `Java`.

* Static Type-Checking

  * <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/Python-Related/Static%20Type-Checking.md">`typing` auxiliary examples</a>

<br>

## License

 This repo is distributed under the <a href="https://github.com/Ziang-Lu/Miscellaneous/blob/master/LICENSE">MIT license</a>.

