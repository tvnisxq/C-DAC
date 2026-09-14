#!/bin/bash

read -p "Enter a number: " num
printf "\n"

if (( num % 2 == 0 )); then
echo "$num is an Even Number!"

else
echo "$num is an Odd Number!"

fi
