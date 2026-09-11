#!/bin/bash

read -p "Enter the principal amount: " p
read -p "Enter the Rate of Interest: " r
read -p "Enter the Time: " t

printf "\n"

echo "Principal is: $p"
echo "Rate of Interest is: $r" 
echo "Time is: $t"

printf "\n"

si=$(( ( p * r * t ) / 100 ))
echo "Simple Interest becomes: $si"

total=$((p + si))
echo "Total Amount becomes: $total"
