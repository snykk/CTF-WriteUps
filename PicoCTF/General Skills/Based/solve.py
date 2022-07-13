import binascii

while True:
	menu = input("binary or decimal [b][d] ? ")
	if menu == "b":
		inputan = input('Inputkan binary: ')
		lists = inputan.split()
		for i in lists:
			n = int(i, 2)
			print(binascii.unhexlify('%x' % n), end="")
		print(end="\n")

	elif menu == "d":
		inputan = input('Inputkan binary: ')
		lists = inputan.split()
		for i in lists:
			n = int(i)
			print(binascii.unhexlify('%x' % n), end="")
		print(end="\n")
