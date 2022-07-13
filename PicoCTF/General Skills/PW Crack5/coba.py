lines = []
with open('dictionary.txt') as f:
	lines = f.readlines()

print(lines[0][:-1])
print(type(lines[0]))
