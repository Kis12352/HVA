#!/bin/bash

<<comment
Replace all the occurences of a to in the first 5 lines of a file, paragraph generated from that site tool.
comment

#let's change the directory
target_directory=$(/home/kishori05/myscripts/shell-scriptingAssignment)

cd "$target_directory" || exit

#display the original content of b.txt
original_content=$(cat b.txt)
echo "Original Content: '$original_content'"

#changing the first 5 occurences of to in first 5 lines
head -n 5 b.txt | sed 's/to/Too/g'


