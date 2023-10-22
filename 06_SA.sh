#!/bin/bash

<<comment
Write the script that does the following,
Find all the processes running on the system owned by root.
print only the process id, cpu percentage of the process as output
write the output of a file in an ascending order of process ids whose name is current timestramp.
comment

#specify the directory
target_directory="/"

#change the directory
cd "$target_directory" || exit 



#find all the processses running in the system owned by root
command_a=$(ps -u root -o pid,pcpu,start_time)

echo "The running processes are: '$command_a' "

#write the output of a file in an ascending order of process ids whose name is current timestramp.
command_b=$(ps -e -o pid,user,%cpu,etime,comm --sort=pid | grep "root" | grep "$(date + '%H:%M')")
echo "output of above command: '$command_b' "

ts="/home/kishori05/myscripts/shell-scriptingAssignment/$(date + "%Y%m%d%H%M%S").txt"

ps -u root -o pid,%cpu, --sort=pid > "$ts.txt"

cat "$ts.txt"
