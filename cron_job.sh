#!/bin/bash

file=games.txt

# number of lines the file has
lines=`cat $file | wc -l`


# Check if any new lines have been added since last time
