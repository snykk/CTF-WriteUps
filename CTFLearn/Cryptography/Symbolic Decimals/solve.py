cipher = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"
lists = cipher.split(',')
dictt = {"!":"1","@":"2","#":"3","$":"4","%":"5","^":"6","&":"7","*":"8","(":"9",")":"0"}

for i in lists:
	temp = ""
	for j in i:
		temp += dictt[j]
	print(chr(int(temp)), end="")
