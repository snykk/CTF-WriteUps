import string

ALPHABET = string.ascii_lowercase[:16] 
encrypted ="lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"

base16 = ["hm" for x in range(len(ALPHABET))]

for i in encrypted:
	for j in range(len(ALPHABET)):
		index = ALPHABET.index(i)
		if(j <= index):
			base16[j]+=chr(index -j+97)
		else:
			base16[j]+=chr(index +16-j+97)

for i in range(len(ALPHABET)):
    flag=""
    b = base16[i]
    for j in range(0, len(b), 2):
        if(b[j+1] in ALPHABET and b[j] in ALPHABET):
            index1 = ALPHABET.index(b[j])
            index2 = ALPHABET.index(b[j+1])
            flag+= chr((index1 <<4) +index2)

    print("="*20)
    print(flag) # we need to check manually for every combination char