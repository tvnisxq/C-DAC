#!/bin/bash

read -p "Enter file Name: " file

if [  -f "$file" ]; then
		printf "\n"
		sleep 1
		echo "File exists!"
		sleep 1
		printf "\n"

		size=$(wc -c < $file )
		lines=$( wc -l < $file )
		words=$( wc -w < $file )
		chars=$( wc -m < $file )

		echo "Size: $size"
		sleep 1
		printf "\n"

		echo "Lines: $lines"
		sleep 1
		printf "\n"

		echo "Words: $words"
		sleep 1
		printf "\n"

		echo "Characters: $chars"
		sleep 1
		printf "\n"

else
		echo "No such file Exists!"

fi
		
