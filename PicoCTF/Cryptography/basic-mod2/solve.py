import string
m = "28 14 22 30 18 32 30 12 25 37 8 31 18 4 37 6 33 34 31 34 36 28 29"
pattern = "@" + string.ascii_uppercase + "0123456789" + "_"
listRes = [pattern[int(x)] for x in m.split()]

print("".join(x for x in listRes))

