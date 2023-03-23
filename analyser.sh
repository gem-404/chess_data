#!/bin/bash


# This module will mark games as either analysed or not analysed.
# If analysed, the games won't be provided for analysis, else
# when a game is requested for analysis, the module will provide
# any of the un-analysed games and mark it as analysed.


dir=/home/ephantus/chess_data/pgn/
analysed_dir=/home/ephantus/chess_data/pgn/analysed/

# Assume no files are analysed at first...
# By adding a "-a" tag at the end of the file name, the pgn file
# is assumed to be analysed.
set file

sel_unmarked_file() {
    # Give a file with no "-a" at the end
    file=`ls $dir | shuf -n 1`
}

# If this module is run, it will give the pgn of a file and mark the
# file appropriately... Hence, at any given time, the file will be checking
# without the given mark to read the pgn.


read_file() {
    # Reads a file and moves it to analysed pgns folder
    cat $dir$1 | xclip -sel clip
    mv $dir$1 $analysed_dir
}

sel_unmarked_file
read_file $file
