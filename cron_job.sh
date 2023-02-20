#!/bin/bash

file=games.txt

# number of lines the file has
lines=`cat $file | wc -l`

# Check for lines that do not conform to the pattern, https://www.chess.com/game/live/69853418297,
# and remove them.
sed -i '/^https:\/\/www\.[a-z]+\.[a-z]+\/[a-z]+\/[a-z]+\/[0-9]\+$/!d' $file

# Check for duplicate lines and remove them
cat $file | sort -u | uniq > $file

# Check if any new lines have been added since last time


# Automatically add, commit and push the changed file to the git repo
