#!/bin/bash

cleaned_csv=$( cut -d ',' -f 2 students.csv | sort | uniq -c )
echo "Number of students enrolled in different Courses:"
printf "\n"
echo "$cleaned_csv"
