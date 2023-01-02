# Dev. & Work Commands

## Unix Commands & Bash Basics

### `tldr`: User-friendly replacement for `man`

>  https://github.com/tldr-pages/tldr
>
> `pip3 install tldr`

```bash
tldr [command]
```



### `printenv`: Print all the environment variables

Some built-in environment variables:

```bash
$USER
$SHELL
$PWD

$HOSTNAME

$RANDOM  # Generate a random number between [0, 2^15-1 (32,767)]
```



### File System Monitoring

#### `df`: Report the disk usage on all currently mounted file systems



#### `du`: Summarize disk usage

```bash
# ~, and print sizes in human-readble format
du -h
```



***

物理开发机满了怎么办？

申请root权限，删除 `/tmp` 下面的一些无用文件：.pch结尾的文件都可以无脑删（krb开头的文件为登录开发机要用的，必须保留，其余都可以删）

***



### File Operations

#### `dirname` / `basename`: Show the directory name, and the filename, respectively



#### `find`: Find files and directories, and perhaps perform subsequent operations on them

```bash
find [where to start searching from] [expression determines what to find] [-options] [what to find]
```

e.g.,

```
GFG
-- demo1
-- demo2
   -- sample.txt
-- demo3
```

```bash
# Search a file with specific name
find ./GFG -name sample.txt

# Search files with pattern
find ./GFG -name *.txt
# ~, and delete them
find ./GFG -name *.txt --delete

# Search for empty files and directories
find ./GFG -empty
```

By using the `-exec`, other UNIX commands can be executed on files or folders found.

```bash
# Search a file with specific name, and delete with confirmation
find ./GFG -name sample.txt -exec rm -i {} \;
```



#### `cat` / `less`: Print out the contents of a file

```bash
cat -n [filename]  # with line numbers

# ~, without loading the entire file into memory
less [filename]

# Overwrite some contents to a file
cat > [filename]
# (command-d to stop inputting)

# Append some contents to a file
cat >> [filename]
```



#### `head` / `tail`: Print out the head/tail-part contents of a file

```bash
head -n 20 [filename]  # top 20 lines

tail -n 20 [filename]  # bottom 20 lines
```



#### `diff`: Compare two files line by line

```bash
diff [file1] [file2]
```



#### `grep`: Search a file for a particular pattern of characters

```bash
grep '^unix' [filename]  # line start/end
grep 'unix$' [filename]

grep -i 'UNix' [filename]  # case insensitive

# (By default, grep matches the given string/pattern even if it is found as a substring in a file.)
grep -w 'unix' [filename]  # only match the whole words in a file

grep -l 'unix' [filename]  # only print out the filenames

grep -n 'unix' [filename]  # also print out the line number

grep -c 'unix' [filename]  # print line counts, rather than the lines themselves
```



#### `sed`

> ```bash
> brew install gnu-sed  # also aliased as 'gsed'
> ```

e.g., 把一个文件的每一行末尾添加 `,`

```bash
cat uids.csv | sed 's/$/,/g' > uids_new
```



#### `tar`: Compress and decompress

```bash
tar -c -zvf source.tar.gz src/
# -c: create archive
# -v: produce verbose output
# -z: compress the resulting archive with gzip
# -f: compress from the given files

tar -t -zvf source.tar.gz
# -t: list archive contents

tar -x -zvf source.tar.gz
# -x: extract from archive
```



### Process Monitoring

#### `top`

```bash
top -u [username]
```



#### `htop`

Similar to `top`, but allows you to scroll vertically and horizontally,  so you can：

- see all the procesess running on the system, along with their full command lines;
- view them as a process tree
- select multiple processes and act on them all at once

```bash
htop -u [username]
```



### Bash Basics & Scripting

```bash
#!/bin/zsh
# Called "shebang"

# ECHO COMMAND
echo "Hello, world!"

# VARIABLES
name="Kevin"
name=$1  # Positional argument
name=$(whoami)  # Execute `whoami`, and put the output in a variable
echo "My name is $name."

# READ USER INPUT
read -p "Enter your name: " username  # A variable is used to receive the user input.
echo "Hello $username, nice to meet you!"

# IF CONDITIONAL
if [ "$username" == "Kevin" ]; then
    echo "Your name is Kevin."
elif [ "$username" == "Brad" ]; then
    echo "Your name is Brad."
else
    echo "Your name is NEITHER Kevin NOR Brad."
fi  # Close the if statement

# COMPARISON OPERATORS
num1=3
num2=5
if [ "$num1" -gt "$num2" ]; then
    echo "$num1 is greater than $num2"
else
    echo "$num1 is less than $num2"
fi
# Valid options: -eq, -ne, -gt, -ge, -lt, -le

# FILE OPERATORS
file="test.txt"
if [ -f "$file" ]; then
    echo "$file is a file"
else
    echo "$file is not a file"
fi
# Valid flags:
# -f file  True if the provided string is a file
# -d file  True if the file is a directory
# -e file  True if the file exists (note that this is not particularly portable, so -f is generally used)
# -s file  True if the file has a non-zero size
# -g file  True if group id is set on the file
# -u file  ... user id ...
# -r file  True if the file is readable
# -w file  ... writable
# -x file  ... executable

# CASE CONDITIONAL
read -p "Are you 21 or over? Y/N " answer  ###
case "$answer" in
    [yY] | [yY][eE][sS])  # Branch 1
        echo "You can have a beer :)"
        ;;
    [nN] | [nN][oO])  # Branch 2
        echo "Sorry, no drinking"
        ;;
    *)  # Default branch
        echo "Please enter y/yes or n/no"
        ;;
esac

# FOR LOOP
names="Kevin Brad Mark"
for name in $names
    do
        echo "Hello $name"
done

# e.g., FOR LOOP TO RENAME FILES
files=$(ls *.txt)  ###
for file in $files
    do
        echo "Renaming $file to new-$file"
        mv $file "new-$file"
done

# WHILE LOOP
line=1
while read -r current_line  ###
    do
        echo "$line: $current_line"
        ((line++))  # (()) does mathematical calculation within it. In this case, increment the variable by 1
done > "./new.txt"

# FUNCTION
function greet() {
    echo "Hello, I am $1 and I am $2"  # Positional parameters
}
greet "Brad" 26
```



## Git Commands

### Repo Operations

```bash
# Initialize the git repo
git init

# Search within the repo for a particular pattern of characters
git grep 'some_keyword' [where to start searching from]
git grep --files-with-matches 'some_keyword' [where to start searching from]  # ~, but only shows the containing files
```



### Branch Operations

```bash
# List all the branches
git branch
git branch -vv  # ~, each with the current commits and its remote-tracking branch

# Switch to a branch
git checkout ziang-local

# Create a branch
git branch ziang-local
# Create the branch, and switch to it
git checkout -b ziang-local

# Create a branch from a remote branch
git checkout -b ziang-local origin/ziang-remote

# Create a branch, and set it to track a remote branch
git branch ziang-local --track origin/ziang-remote
git checkout -b ziang-local --track origin/ziang-remote

# Delete a branch
git branch -d ziang-local
git branch -D ziang-local
# => git branch -d --force ziang-local

# Delete a remote branch
git push origin --delete ziang-remote
```



### Modification Operations

#### Basic Illustration

![git_workflow](https://github.com/Ziang-Lu/Miscellaneous/blob/master/git_workflow.png?raw=true)



#### Unstage

```bash
# Unstage a staged file
git reset <file>
# <=> git reset HEAD <file>
# <=> git restore --staged <file>

# Unstage all the staged files
git reset
# <=> git reset HEAD
# <=> git restore --staged
# Essentially, reset the stage area
```



#### Discard Changes

```bash
# Discard the changes of a unstaged file
git checkout -- <file>
# Essentially, discard the changes of a unstaged <file> to be the same as HEAD commit

# Discard the changes of a staged file
git reset --hard <file>
# <=> git reset --hard HEAD <file>
# <=> git restore --HEAD <file>
```



#### Examine the Status & Difference

```bash
# Examine the current status
git status

# Examine the difference between the unstaged changes and the HEAD commit
git diff
git diff --stat  # Generate a diffstat
git diff --numstat  # ~, but shows the number of added and deleted lines in decimal notation

# Examine the difference between the staged changes and the HEAD commit
git diff --staged
# <=> git diff --cached
```



#### Fix Commit Message of a Committed Commit

```bash
# git commit -m "Wrong commit message"
git commit --amend -m "Correct commit message"
```

If we accidentally forgot to add a file that should've been included to a commit, we can also use `--amend`:

```bash
# git commit -m "some message"
# git touch some_file
# git add some_file
git commit --amend
# Now the commit contains the newly created file.
```



#### `stash`

````bash
# Stash all the changes in the working area and stage area (i.e., all the uncommitted changes)
git stash

# Stash the changes in the working area, but keep the changes in the stage area
git stash --keep-staged
````



#### `cherry-pick`

Check out https://www.youtube.com/watch?v=-ndmel-4wsk

```bash
git checkout ziang-local
git cherry-pick <commit>
```



### Commits History Operations

#### `log`

```bash
# List the full commit logs
git log

# List the commit logs, one-line for each
git log --pretty=oneline
git log --oneline
# <=> git log --pretty=oneline --abbrev-commit

# List the commit logs with a format
git log --pretty=format:%ae  # %ae: placeholder for "author email"

# List the commit logs (diff-based)
git log --stats

git log --author=[pattern]
```



#### Reset Branch

e.g.,

```bash
# Current commits history:
# commit_hash_2
#  added some_file_2
# commit_hash_1
#  added some_file_1
```

```bash
git reset --soft commit_hash_1
# Reset to commit_hash_1, with some_file_2 in the stage area

git reset --mixed commit_hash_1  # default mode

git reset --hard commit_hash_1
```



#### `rebase`

Check out https://www.youtube.com/watch?v=TymF3DpidJ8

```bash
git checkout ziang-local
git rebase master
```

