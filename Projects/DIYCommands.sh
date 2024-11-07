#!/bin/bash

#Standard output
echo "Linux" > file.txt

#Standard input
pwd < file.txt

#Both Standard output and Standard input
cat < file.txt > myfile.txt

#Standard error
ls /fake/directory 2> file.txt

#Both Standard error and Standard output in file.txt
ls /fake/directory > file.txt 2>&1

#Shortcut for both standard error and standard output
ls /fake/directory &> file.txt
