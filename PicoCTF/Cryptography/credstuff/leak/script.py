import string
cipher = "cvpbPGS{P7e1S_54I35_71Z3}"
abj = string.ascii_uppercase

for i in cipher:
	if i.isalpha():
		loc = abj.index(i.upper())
		loc += 13
		loc %= 26
		if i.isupper():
			print(abj[loc], end="")
		else:
			print(abj[loc].lower(), end="")
	else:
		print(i, end="")
