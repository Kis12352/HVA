#!/bin/bash

#Count the number of times the letter exits in a file irrespective of the case of the letter. Both the file and letter should be taken as input.

#let's change the directory

target_directory="/home/kishori05/myscripts/shell-scriptingAssignment"

cd "$target_directory" || exit

#command for counting letter t
command=$(tr '[:upper:]' '[:lower:]' < b.txt | grep -o 't' | wc -l)
echo "t is coming '$command' times."
