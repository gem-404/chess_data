#!/bin/bash

file=./games.txt


# Runs the curl command silently, and outputs the results to games2.html

cat games.txt | xargs -I {} curl -s -o games2.html {}