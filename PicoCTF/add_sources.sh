ARG=$1

if [ -z "$ARG" ]
then
	echo -n "Masukkan nama challenge: " 
	read ARG
fi

git add .
git commit -m "Add \"$ARG\" sources"

