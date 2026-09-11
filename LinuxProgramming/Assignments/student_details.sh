#!/bin/bash

# Input Prompt and reading happens in the same line using -p  
read -p "Enter your Name: " name

read -p "Enter your Age: " age

read -p "Student's Marks for 3 subjects: " m1 m2 m3

# Echoing with prompt
echo "Name: $name"
echo "Age: $age"

echo "Marks1: $m1"
echo "Marks2: $m2"
echo "Marks3: $m3"

# Echoing a \n for better output readability

#NOTE: The echo "\n" character will display a line gap when run via the 
#student_details.sh but won't when run via the ./student_details.sh

printf "\n"


echo "Average becomes: $(( (m1 + m2 + m3) / 3 ))"