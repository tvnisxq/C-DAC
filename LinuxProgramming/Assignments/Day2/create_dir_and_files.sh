#!/bin/bash

read -p "Enter the name of the Directory: " dir_name
printf "\n"
sleep 1
mkdir $dir_name
echo "Directory "$dir_name" created!"

read -p "Enter the name of the 5 files: " file1 file2 file3 file4 file5
printf "\n"
sleep 1
touch $dir_name/$file1 $dir_name/$file2 $dir_name/$file3 $dir_name/$file4 $dir_name/$file5
echo "Files created inside $dir_name/"



count=0
for file in "$dir_name"/*; do
		if [ -f "$file" ]; then
				sleep 1
				echo "$file"
				(( count++ ))
		fi
done
sleep 1
printf "\n"

echo "Total Number of files: $count"
