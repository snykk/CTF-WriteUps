f = open("passwords.txt", "r")

for i, j in enumerate(f.readlines(), 1):
        j = j[:-1]
        print(f"{i} {j}")
        if i == 378:
                break
