read -p "Enter a number: " num
printf "\n"

if [ $num -gt 0 ]
then 
echo "$num is a Positive Number!"

elif [ $num -lt 0 ] 
then
echo "$num is a Negative Number"

else
echo "Entered Number is a zero"

fi

