#!/bin/bash

folder=./chess_pgn

for file in `ls $folder`; do

    without_ext=`echo $file | cut -d. -f1`

    filename_len=`expr length $without_ext`

    let new_len=$filename_len-2

    new_file=`expr substr $without_ext $new_len $filename_len`

    echo $file
    mv  $folder/$file $folder/$new_file.txt

done

