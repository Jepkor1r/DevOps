#!/bin/bash

#if else

weather=rain
name=$1
package=which

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

if command -v $package
then
	pkg install -y $package >> package_install_results.log
	echo "Installation of $package is successful."
	echo "The exit status code is: $?"
	which $package
else
	echo "$package failed to install" >> package_install_failure.log
fi
