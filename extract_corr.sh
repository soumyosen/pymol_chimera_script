#!/bin/bash
########### run by "bash etract_corr.sh" 
arr_logfiles=()


for file in *.log
do
	arr_logfiles=(${arr_logfiles[@]} "$file")
done

echo "${arr_logfiles[@]}"

for file1 in "${arr_logfiles[@]}"
do
	echo $file1
	output=$( tail -n 2 $file1 | awk '{print $4, $10}' )
	#output=$(awk 'END{print}' $file1)
	#output1=${output::-2}
	echo $output >> cross_corr.txt
done


