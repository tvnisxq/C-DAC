#!/bin/bash

read -p "Enter the directory name: " dir
read -p "Enter the file extension: " ext
printf "\n"

if [ -d "$dir" ]; then
		echo "Searching inside $dir for all "$ext files..." "
		printf "\n"
		sleep 2

		files=$(find "$dir" -type f -name "*.$ext")
		printf "\n"
		echo "$files"
		sleep 1
		

		count=$( echo "$files" | wc -l )
		sleep 1
		printf "\n"
		echo "Total $ext files: $count"
		
else
		echo "Directory doesn't exist!"	

fi
