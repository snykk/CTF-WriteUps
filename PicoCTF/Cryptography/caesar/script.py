abj = "abcdefghijklmnopqrstuvwxyz"
strr = "dspttjohuifsvcjdpoabrkttds"
new = ""
for i in range(1, 27):
	for j in strr:
		loc = abj.index(j)
		loc += i
		loc %= 26
		new += abj[loc]
	print(new)
	new = ""
