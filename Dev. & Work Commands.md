# Dev. & Work Commands

## Unix Commands & Bash Basics

### `tldr`: User-friendly replacement for `man`

>  https://github.com/tldr-pages/tldr
>
> `pip3 install tldr`

```bash
tldr [command]
```



### `env` / `printenv`: Print all the *global* environment variables

Some built-in environment variables:

```bash
$USER
$SHELL  # Locationof current user's shell program

$HOME
$PWD

$PATH  # Search path for commands

$LANG  # Default system language

$HOSTNAME

$RANDOM  # Generate a random number between [0, 2^15-1 (32,767)]
```

Use `export` to export a local variable to global



### Bash Basics & Scripting

```bash
#!/bin/zsh
# Called "shebang"

# LOCAL variables
NAME="Kevin"
NAME=$1  # Positional argument
NAME=$(whoami)  # Execute `whoami`, and put the output in a variable
echo "My name is $NAME."

# Read user input
read -p "Enter your name: " USERNAME  # A variable is used to receive the user input.
echo "Hello $USERNAME, nice to meet you!"

# If conditional
if [ "$USERNAME" == "Kevin" ]; then
    echo "Your name is Kevin."
elif [ "$USERNAME" == "Brad" ]; then
    echo "Your name is Brad."
else
    echo "Your name is NEITHER Kevin NOR Brad."
fi  # Close the if statement

# Comparison operators
NUM1=3
NUM2=5
if [ "$NUM1" -gt "$NUM2" ]; then
    echo "$NUM1 is greater than $NUM2"
else
    echo "$NUM1 is less than $NUM2"
fi
# Valid options: -eq, -ne, -gt, -ge, -lt, -le

# File operators
FILE="test.txt"
if [ -f "$FILE" ]; then
    echo "$FILE is a file"
else
    echo "$FILE is not a file"
fi
# -f file  True if the provided string is a file
# -d file  True if the file is a directory
# -e file  True if the file exists (note that this is not particularly portable, so -f is generally used)
# -s file  True if the file has a non-zero size
# -g file  True if group id is set on the file
# -u file  ... user id ...
# -r file  True if the file is readable
# -w file  ... writable
# -x file  ... executable

# Case conditional
read -p "Are you 21 or over? Y/N " ANSWER  ### -> callback to above
case "$ANSWER" in
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

# For loop
NAMES="Kevin Brad Mark"
for name in $NAMES
    do
        echo "Hello $NAME"
done
# e.g., for loop to rename files
FILES=$(ls *.txt)  ### -> callback to above
for file in $FILES
    do
        echo "Renaming $FILE to new-$FILE"
        mv $FILE "new-$FILE"
done

# While loop
LINE=1
while read -r CURRENT_LINE  ### -> callback to above
    do
        echo "$LINE: $CURRENT_LINE"
        ((LINE++))  # (()) does mathematical calculation within it. In this case, increment the variable by 1
done > "./new.txt"

# Function
function greet() {
    echo "Hello, I am $1 and I am $2"  # Positional parameters
}
greet "Brad" 26
```



### System Monitoring

#### `free`: Memory usage report

```bash
free -g  # ~, and print sizes in gigabytes
# Valid size options: -b / -k (This is the default.) / -m / -g

free -h  # ~, and print sizes in human-readable format

free -t  # ~, and also report a total line
```



#### `top` / `htop`: Processes with top usage report

`htop` is similar to `top`, but stronger.

```bash
htop -p [process_id]

htop -U [username]

# By default, sort by CPU usage
htop -U [username] -o cpu
# Valid sort-key options: pid / cpu / mem / threads
```



#### `df`: Disk usage (on all currently mounted file systems) report

```bash
df -h  # ~, and print sizes in human-readable format (power of 1024)
```



#### `du`: Disk usage (by files and directories) report

```bash
du -h  # ~, and print sizes in human-readable format (power of 1024)

du -a  # Display an entry for each file in a file hierarchy
```

With `sort`, report the disk usage by files and directories <u>sorted by top sizes</u>

```bash
du -ha [directory_name] | sort -nr
```



***

物理开发机满了怎么办？

申请root权限，删除 `/tmp` 下面的一些无用文件：.pch结尾的文件都可以无脑删（krb开头的文件为登录开发机要用的，必须保留，其余都可以删）

***



### File Operations

#### `dirname` / `basename`: Show the directory name, and the filename, respectively

e.g.,

```bash
# basename without a specified trailing suffix
basename 'include/stdio.h' .h  # <=> basename -s .h 'include/stdio.h'
# "stdio"
```



#### `find`: Search for files and directories

```bash
find [where_to_search_from] [expression_determining_what_to_find] [-options] [what_to_find]
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
# Search for a file with a specific name
find ./GFG -name sample.txt

# Search for files with a specific name pattern
find ./GFG -name *.txt
# ~, and delete them
find ./GFG -name *.txt --delete

# Search for files with specific permission
find ./GFG -perm /a=x

# Search for empty files and directories
find ./GFG -empty
```

<u>By using the `-exec`, other UNIX commands can be executed on files or folders found.</u>

```bash
# Search a file with specific name, and delete with confirmation
find ./GFG -name sample.txt -exec rm -i {} \;
```



#### `cat` / `less`: Print the contents of a file

`less`: ~, without loading the entire file into memory

```bash
cat/less -n [filename]  # ~, with line numbers

cat/less -s [filename]  # ~, and squeeze adjacent empty lines

# Overwrite some contents, to a file
cat > [filename]  # (command-d to stop inputting)
# Overwrite the contents of file1, to file2
cat [file1] > [file2]
# Merge the contents of file1, file2, file3, to file4
cat [file1] [file2] [file3] > [file4]

# Append some contents, to a file
cat >> [filename]
# Append the contents of file1, to file2
cat [file1] >> [file2]
```



#### `head` / `tail`: Print the head/tail-part contents of a file

```bash
head -n 20 [filename]  # ~, with top 20 lines

tail -n 20 [filename]  # ~, with bottom 20 lines
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

grep -l 'unix' [filename]  # only print the filenames

grep -n 'unix' [filename]  # also print the line number

grep -c 'unix' [filename]  # print line counts, rather than the lines themselves
```



#### `awk`: 

```bash
awk '{print $2}'
```



#### `sed`

> ```bash
> brew install gnu-sed  # also aliased as 'gsed'
> ```

e.g., 把一个文件的每一行末尾添加 `,`

```bash
cat uids.csv | sed 's/$/,/g' > uids_new
```



#### `sort`: Sort a file (without actually changing it in-place)

```bash
sort [filename]

sort [filename] > [sorted_output_filename]

# By default, blank lines or newline characters are used as record separators.
sort -t '\t' [filename]  # ~, with '\t' as the record separator

# By default, sort by ASCII codes
sort -b [filename]  # ~, ignoring leading blank characters
sort -f [filename]  # ~, ignoring cases
sort -n numbers.txt  # ~, numerically

sort -r [filename]  # ~, in reverse order

sort -u [filename]  # ~, and remove duplicates
```



#### `tar` / `zip` & `unzip`: Compress and decompress

e.g.,

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

zip source.zip src/

unzip source.zip
```



### Networking

#### `ip`: Check out IP address

```bash
ip address
```



####  `curl` / `wget`: File downloading / retrieving

```bash
curl -L [file_url]  # download [file_url], and print to stdout
curl -L [file_url] > [output_filename]  # ~, and dump to [output_filename]

wget [file_url]  # download [file_url]
wget -O - [file_url]  # ~, and print to stdout
wget -O [output_filename] [file_url]  # ~, and dump to [output_filename]
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

