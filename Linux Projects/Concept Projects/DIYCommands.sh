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



#find(searches), .(current directory), -name "*.txt"(file names that ends with .txt, *(all)), ls(list in long format).
find . -name "*.txt" -ls


#Alias is a new command thats acts as an  abbreviation of the longer command
#alias new-name='command-value'
alias l='ls -l'

#A->Days of the week, B->Month, d->day of the month, Y->Year
alias today='date +"%A, %B %-d, %Y"'

#X->time in 24h, Y->Year, Z->Time zone
alias time='date +"%X, %Y, %Z"'

#checks for execution status: success is 0 whie failure is any non-zero value. Non -existing file returns 2.
echo $?

#outputs the default shell for the current user
echo $SHELL

#variable
myname="Lagat"
echo "Hello $myname!"

#$() enclosing inner command---> Command substitution
#uname is used to show system info, -r specifically outputs the kernel release version.
ls /lib/modules/$(uname -r)/

#exporting variable
export VAR=value

export | head -20

#Path is the list of directories; To view list of directories > echo $PATH
echo $PATH

#Add directory to your own path
export PATH=$PATH:/path/to/add_directory


#math functions
expr 10 + 30

expr 10 \* 30

num1=10
num2=10
expr $num1 - $num2

#fetches real time weather info( /Nairobi, to append city )
curl wttr.in/Nairobi
