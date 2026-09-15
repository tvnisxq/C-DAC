#!/bin/bash

read -p "Enter the directory name: " dir_name
read -p "Enter the extension to search for files: " ext
printf "\n"

if [ -d $dir_name ]; then
		echo "Searching inside $dir_name for all the "$ext files..." "
		sleep 1

		files=$( find "$dir_name" -type f -name "*.$ext" )
		printf "\n"
		echo "$files"
		sleep 1

	

else
	echo "No such directory exists!"

fi	
