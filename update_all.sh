#! /bin/bash

FOLDERS=$(ls)
for FOLDER in $FOLDERS
    do
        if [ -d $FOLDER ]; then
            echo "Entering and updating $FOLDER"
            cd $FOLDER
            git pull
            cd ..
        fi
        sleep 1s
done
