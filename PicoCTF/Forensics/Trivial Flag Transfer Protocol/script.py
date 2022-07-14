abj = "abcdefghijklmnopqrstuvwxyz"
instruction = "GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA"
plan = "VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF"

def brute_force_decrypt_caesar(abj, cipher):
	result  = ""
	for i in range(1, 27):
		for j in cipher.lower():
			if j.isalpha():
				loc = abj.index(j)
				loc += i
				loc %= 26
				result += abj[loc]
			else :
				result += j
		print(result)
		result = ""

print("===============================================> INSTRUCTIONS <=========================================")
print(brute_force_decrypt_caesar(abj, instruction))
print("===================================================> PLAN <=============================================")
print(brute_force_decrypt_caesar(abj, plan))
