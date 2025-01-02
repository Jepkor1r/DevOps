#!/bin/bash

#while loop

myvar=1

while [ $myvar -le 10 ]
do
	echo $myvar
	myvar=$(( $myvar +1 ))
done

while [ -f ~/myfile ]
do
	echo "As for $(date), my file exists."
done

echo "As of $(date), my file has gone missing."

