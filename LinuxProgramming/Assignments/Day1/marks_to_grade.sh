#!/bin/bash

read -p "Enter Student's Marks: " marks

printf "\n"


echo "According to the following Grading slabs:"
echo "90–100 → Grade A"
echo "75–89 → Grade B"
echo "60–74 → Grade C"
echo "50–59 → Grade D"
echo "Below 50 → Fail"

printf "\n"

if [ $marks -gt 100 ]; then
echo "Invlid Value for marks"

elif [ $marks -ge 90 ]; then
echo "---> Student has acquired an A Grade"

elif [ $marks -ge 75 ]; then
echo "---> Student has acquired a B Grade"

elif [ $marks -ge 60 ]; then
echo "---> Student has acquired a C Grade"

elif [ $marks -ge 50 ]; then
echo "---> Student has acquired a Grade D"

else
echo "---> Student has Failed the Exam"

fi



