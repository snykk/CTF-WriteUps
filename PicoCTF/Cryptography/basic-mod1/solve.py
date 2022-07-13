import string

iniStr = "128 63 131 198 262 110 309 73 276 285 316 161 151 73 219 150 145 217 103 226 41 255"
listChar = iniStr.split()
pattern = string.ascii_uppercase + "0123456789" + "_"



fixMod = [ pattern[int(x)%37] for x in listChar]
print("".join(x for x in fixMod))
