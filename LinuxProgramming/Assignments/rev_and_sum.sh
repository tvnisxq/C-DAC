#!/bin/bash

read -p "Enter a Number: " num

printf "\n"

sum=0
reverse=0

while [ $num -gt 0 ]
do

digit=$(( num % 10 ))
sum=$(( sum + digit ))
reverse=$(( ( reverse * 10 ) + digit ))
num=$(( num / 10 ))
done 


echo "Sum of digits: $sum"
printf "\n"
echo "Reverse: $reverse"

