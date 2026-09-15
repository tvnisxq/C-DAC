#!/bin/bash

read -p "Enter the directory name: " dir

if [ -d $dir ]; then
		printf "\n"
		sleep 1
		echo "Directory Exists!"
		sleep 1

		echo "Directory Contents: "
		ls $dir/


else
		echo "Directory doesn't exist!"
		printf "\n"
		sleep 1
		
		echo "Creating Directory $dir..."
		sleep 1
		mkdir $dir
		
		echo "Directory Contents: "
		ls $dir/

fi
