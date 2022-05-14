abj = "abcdefghijklmnopqrstuvwxyz"
strr = "OD5355{fdhvdu_F76V7U}"
new = ""
for i in range(1, 27):
	for j in strr:
		if (j in abj):
			loc = abj.index(j)
			loc += i
			loc %= 26
			new += abj[loc]
		else :
			new += j
	print(new)
	new = ""
