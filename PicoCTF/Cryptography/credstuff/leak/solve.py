f = open("usernames.txt", "r")

for i, j in enumerate(f.readlines(), 1):
	j = j[:-1]
	print(f"{i} {j}")
	if j == "cultiris":
		break
	
	
