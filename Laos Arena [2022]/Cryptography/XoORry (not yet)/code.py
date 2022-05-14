from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes
from os import urandom

Flag = open("flag.txt","rb").read().strip()
key = urandom(len(Flag))
key1 = urandom(len(Flag))
m = bytes_to_long(Flag)
k = bytes_to_long(key)
k1 = bytes_to_long(key1)

print(m^k)
print(k^k1)
print(k1)
# printed on output.txt
