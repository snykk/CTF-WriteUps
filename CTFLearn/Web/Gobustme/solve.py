import requests

#r = requests.post("https://gobustme.ctflearn.com/flag")
#print(r.content)
lists = []
with open("wordlists.txt", 'r') as f:
	lists = f.readlines()

for i in lists:
	url = "https://gobustme.ctflearn.com/" + i[:-1]
	r = requests.post(url)
	print(url)
	if "404 Not Found" not in r.content:
		print(r.content)
		print("\n=======================================")
