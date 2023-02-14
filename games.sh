#!/bin/bash

file=./games.txt


cat games.txt | xargs -I {} curl -s -o games2.html {}

