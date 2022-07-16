lists = []
with open("data.dat","r") as f:
	lists = f.readlines()
cek = 0
for i in lists:
	if (i[:-1].count("0") % 3 == 0 or i[:-1].count("1") % 2 == 0):
		cek += 1

print(cek)
