#!/bin/bash

read -p "Enter the Number: " n

sum=0
count=0

i=1

while [ $i -le $n ]
do
	# Check if i is even
	if [ $((i % 2)) -eq 0 ]; then
		even_sum=$((even_sum + i))
	fi
	
	# Check if i is divisible by 5
	if [ $(( i % 5)) -eq 0 ]; then
		count=$((count + 1))
		printf "\n"
		echo "Divisible by 5: $i"

	fi
	
	i=$((i + 1))

done


printf "\n"
echo "Sum of even natural numbers: $even_sum"
printf "\n"
echo "Count of numbers divisible by 5: $count"
printf "\n"
# If you are asked to display the individual numbers as well
