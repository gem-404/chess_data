#!/bin/bash

file=/home/ephantus/chess_data/games.txt
pyfile=/home/ephantus/chess_data/games.py

# check how many lines $file currently has.
lines_in_file=`cat $file | wc -l`

args=`xclip -selection clipboard -o`

# Reads whatever is in the clipboard and appends it in the games.txt file.

echo "$args" >> $file


last_line=`tail -1 $file`

new_lines=`cat $file | wc -l`

if [ "$new_lines" -ge "$lines_in_file" ]; then

    # we will need to check if a game was added by using a notify-send
    notify-send "Added a game" "Game $last_line was added..."

fi

# Remove all duplicate entries in the main file -> games.txt
sort $file | uniq > tmpfile && mv tmpfile $file

pyfile
