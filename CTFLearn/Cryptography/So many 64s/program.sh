#! /bin/bash

#base64 -d flag.txt > output
#while true 
#do
#	base64 -d output > output
#	if ( cat output | grep "CTFlearn" ) then
#	break
#	fi
#done
cat flag.txt > cipher
while true
do 
	base64 -d cipher > dumy
	cat dumy > cipher
	cat dumy
done
