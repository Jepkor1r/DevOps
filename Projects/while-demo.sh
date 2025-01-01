#!/bin/bash

#while loop

myvar=1

while [ $myvar -le 10 ]
do
	echo $myvar
	myvar=$(( $myvar +1 ))
done
