#!/bin/bash

read -p "Enter the directory name: " dir
read -p "Enter the file extension: " ext

if [ -d "$dir" ]; then
echo "Searching inside $dir for all "$txt files..." "
sleep 2

files=$(( find $dir -type f -name ".$ext" ))
sleep 1
echo "$files"

count=$(( $files | ( wc -l ) ))
sleep 1
echo "$count"
		
else
echo "Directory doesn't exist!"	

fi


