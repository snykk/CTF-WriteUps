#!/usr/bin/env python3

import binascii

def dec(msg, key):
    '''
    Simple char-by-char XOR with a key (Vigenere, Vernam, OTP)
    '''
    m = ""
    for i in range(0, len(key)):
        m += chr(msg[i] ^ ord(key[i]))
    return m

######################################

lines = []

with open("msg","r") as f:
    # Read lines from file and decode Hex
    ls = f.readlines()
    for l in ls:
        lines.append(binascii.unhexlify(l[:-1]))

# Step 1: Decode each line with the known key
k = "ALEXCTF{"
mes = []
for l in lines:
    m = dec(l,k)
    mes.append(m)
print(mes)

# Step 2: Guess some part of the first message 'Dear Fri'
k = "Dear Friend, "
m = dec(lines[0],k)
print(m)

# Step 3: Decode each line with the new known key
k = "ALEXCTF{HERE_"
mes = []
for l in lines:
    m = dec(l,k)
    mes.append(m)
print(mes)

# Step 4: Guess some part of the last message 'ncryption sc'
k = 'ncryption scheme '
m = dec(lines[-1],k)
print(m)

# Step 5: Decode each line with the new known key
k = "ALEXCTF{HERE_GOES_"
mes = []
for l in lines:
    m = dec(l,k)
    mes.append(m)
print(mes)

# Step 6: Guess all the second message 'sed One time pad e'
# the third message is 'n scheme, I heard '
# so we can retrive the complete key
k = 'sed One time pad encryptio'  
m = dec(lines[2],k)
print(m)
