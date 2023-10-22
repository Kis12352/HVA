#!/bin/bash

<<comment
Find and replace
a word in a file and verify
only the first 5 occurences 
multiple words with one word
comment

#let's change the directory
target_directory="/home/kishori05/myscripts/shell-scriptingAssignment"

cd "$target_directory" || exit

#Display the original content of a.txt
original_content=$(cat a.txt)
echo "Original Content: '$original_content' "

#find and replace a word in a file using sed in a.txt
sed -i 's/Foo/cook/g' a.txt

#Display the messagae to indicate the replacement
echo "Replacement completed"

#verify the changed content
changed_content=$(cat a.txt)
echo "Changed Content: '$changed_content' "

#only the first 5 occurences of the word

sed -i 's/She/he/1;s/She/he/2;s/She/he/3;s/She/He/4;s/She/he/4;s/She/he/5' a.txt

#Display the message to indicate the replacement
echo "Replacement Completed"

#verify the changed content
changed_content=$(cat a.txt)
echo "Changed content: '$changed_content'"

#multiple words with one word
sed -i 's/fell\|left/caught/g' a.txt

#verify the changed content
changed_content=$(cat a.txt)
echo "Changed content; '$changed_content'"

