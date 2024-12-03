#!/bin/bash

#if else

weather=rain
name=$1

if [ $weather == rain ]
then
	echo "Yes, its raining!"
else
	echo "Nah, its not raining!"
fi

if [ "$name" = "" ]
then
	echo "Enter search name: "
	read name
fi
