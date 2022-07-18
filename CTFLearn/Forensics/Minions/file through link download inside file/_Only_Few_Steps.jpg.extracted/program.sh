
cat flag_string | sed 's/.*{//' | sed 's/}//' > cipher

while true
do
	base64 -d cipher > dummy
	cat dummy > cipher
	cat dummy
	echo 
done
