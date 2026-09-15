#!/bin/bash

read -p "Enter directory name: " dir

mkdir -p report

files=$(find "$dir" -type f | wc -l)
dirs=$(find "$dir"  -mindepth 1 -type d | wc -l)
lines=$(find "$dir"/* 2>dev/null } wc -l)

echo "Files: $files" > report/summary.txt
echo "Directories: $dirs" >> report/summary.txt
echo "Lines: $lines $lines" >> report/summary.txt

cat report/summary.txt
