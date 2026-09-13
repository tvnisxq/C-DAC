#!/bin/bash

read -p "Enter the directory name: " dir
printf "\n"

mkdir $dir
sleep 1
echo "Directory created!"

read -p "Enter the name of three files: " file1 file2 file3
printf "\n"

touch $dir/$file1 $dir/$file2 $dir/$file3
sleep 1
echo "Files $file1, $file2, $file3 Created inside $dir/"

printf "\n"
sleep 1
echo "Directory Contents: "
ls $dir/
