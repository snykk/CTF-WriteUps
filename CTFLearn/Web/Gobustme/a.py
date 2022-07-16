lists = []
with open("wordlists.txt", 'r') as f:
        lists = f.readlines()

print(len(lists))
