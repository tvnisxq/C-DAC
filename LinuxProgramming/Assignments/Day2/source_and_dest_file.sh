#!/bin/bash

read -p "Enter Source File Name: " src
read -p "Enter Destination File Name: " dest

if [ -f $src ]; then
		printf "\n"
		echo "Source File Exists!"
		sleep 1

		cp $src $dest
		echo "$src copied into $dest!"
		
else
		echo "No Source File Present!"

fi

