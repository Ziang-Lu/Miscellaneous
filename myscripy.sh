#! /bin/bash

# ECHO COMMAND
# echo "Hello, world!"

# VARIABLES
# NAME="Kevin"  # Uppercase by convention
# echo "My name is $NAME."

# USER INPUT
# read -p "Enter your name: " USERNAME  # A variable is used to receive the user input.
# echo "Hello $USERNAME, nice to meet you!"

# IF CONDITIONAL
# if [ "$USERNAME" == "Kevin" ]; then
#     echo "Your name is Kevin."
# elif [ "$USERNAME" == "Brad" ]; then
#     echo "Your name is Brad."
# else
#     echo "Your name is NEITHER Kevin NOR Brad."
# fi  # Close the if statement

# COMPARISON OPERATORS
# NUM1=3
# NUM2=5
# if [ "$NUM1" -gt "$NUM2" ]; then
#     echo "$NUM1 is greater than $NUM2"
# else
#     echo "$NUM1 is less than $NUM2"
# fi
# Valid options: -eq, -ne, -gt, -ge, -lt, -le

# FILE OPERATORS
# FILE="test.txt"
# if [ -f "$FILE" ]; then
#     echo "$FILE is a file"
# else
#     echo "$FILE is not a file"
# fi
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
# read -p "Are you 21 or over? Y/N " ANSWER
# case "$ANSWER" in
#     [yY] | [yY][eE][sS])  # Branch 1
#         echo "You can have a beer :)"
#         ;;
#     [nN] | [nN][oO])  # Branch 2
#         echo "Sorry, no drinking"
#         ;;
#     *)  # Default branch
#         echo "Please enter y/yes or n/no"
#         ;;
# esac

# FOR LOOP
# NAMES="Kevin Brad Mark"
# for NAME in $NAMES
#     do
#         echo "Hello $NAME"
# done

# FOR LOOP TO RENAME FILES
# FILES=$(ls *.txt)  # List all the files with ".txt" extension, and put them in a variable
# for FILE in $FILES
#     do
#         echo "Renaming $FILE to new-$FILE"
#         mv $FILE "new-$FILE"
# done

# WHILE LOOP
# LINE=1
# while read -r CURRENT_LINE
#     do
#         echo "$LINE: $CURRENT_LINE"
#         ((LINE++))  # Increment the variable by 1
# done < "./new-1.txt"

# FUNCTION
function greet() {
    echo "Hello, I am $1 and I am $2"  # Positional parameters
}
greet "Brad" 26
