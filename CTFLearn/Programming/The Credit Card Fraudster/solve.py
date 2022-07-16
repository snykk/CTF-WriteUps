#The little flower shop
#======================

#European Express Debit
#Card Number: 543210******1234
#SALE

#Please debit my account
#Amount: 25.00€

from luhn import verify

maks = 5432110000001234
min = 5432100000001234
start = (min//123457)*123457
lists = []
while start < maks:
	start += 123457
	if start%10000 == 1234 and verify(str(start)):
		lists.append(start)
print(lists)
