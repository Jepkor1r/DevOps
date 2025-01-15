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
ls /fake/directory &> file.txt

#find(searches), .(current directory), -name "*.txt"(file names that ends with .txt, *(all)), ls(list in long format).
find . -name "*.txt" -ls

#checks for execution status: success is 0 whie failure is any non-zero value. Non -existing file returns 2.
echo $?

#"-e" is for exists, grep is for searching
grep -e "Linux" file.txt

#make(build automation tool). Heard of makefile before? Huh!
#chaining commands. first (;) allows the execution of commands even if the preceding one fails
make; make install; make clean
#secondly (&&) allows you to abort subsequent command when earlier one fails
make && make install && make clean
#thirdly (||) allows that if the first command fails the second never executes
make || make install || make clean

# wc(counts the number of lines, words and character in a file)
wc file.txt 
# wanna do input redirection?
wc < file.txt
#or may just piping it?
cat file.txt | wc