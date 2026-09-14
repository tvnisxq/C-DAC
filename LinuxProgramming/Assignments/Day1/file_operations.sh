#!/bin/bash

read -p "Enter the file name: " file

if [ -f $file ]; then # Checking whether the file exists or not
		sleep 1
		echo "File exists!" 
		printf "\n"


		size=$( wc -c < $file )
		sleep 1
		echo "File Size: $size"
		printf "\n"

		lines=$( wc -l < $file )
		sleep 1
		echo "Number of lines in $file: $lines"
		printf "\n"

		words=$( wc -w < $file )
		sleep 1
		echo "Number of words in $file: $words"
		printf "\n"
		

		chars=$( wc -m < $file )
		sleep 1
		echo "Number of characters in $file: $chars"
		printf "\n"

else
echo "No such file exists!"

fi

