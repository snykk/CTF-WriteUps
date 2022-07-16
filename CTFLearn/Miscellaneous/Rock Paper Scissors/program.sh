#!/bin/bash
file="./answer"
while IFS= read -r line
do
	echo "$line"
done < $file
