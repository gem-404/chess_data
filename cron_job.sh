#!/bin/bash

file=/home/ephantus/chess_data/games.txt
pyfile=/home/ephantus/chess_data/games.py

# number of lines the file has
lines=`cat $file | wc -l`

# Check for lines that do not conform to the pattern, https://www.chess.com/game/live/69853418297,
# and remove them.
# sed -i '/^https:\/\/www\.[a-z]+\.[a-z]+\/[a-z]+\/[a-z]+\/[0-9]\+$/!d' $file

# Check for duplicate lines and remove them
sort $file | uniq > tmpfile && mv tmpfile $file

# Check if any new lines have been added since last time
while : do

    if [ -N $file ]; then
        newlen=`wc -l $file | awk '{ print $1 }'`
        newlines=`expr $newlen - $lines`

        if [ $newlines -gt 0 ]; then
            python $pyfile
        fi

        lines=$newlen

        # Automatically add, commit and push the changed file to the git repo
        git add games.txt pgn/ ; git commit -m "Added a url to games.txt and a pgn file..."

        sleep 300

    fi

done

