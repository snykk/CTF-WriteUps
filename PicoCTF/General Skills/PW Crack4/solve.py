import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

flag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_4_pw_check(user_pw):
    print("Please enter correct password for flag: ", user_pw)
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return True
    print("That password is incorrect")



#level_4_pw_check()



# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["b5e5", "71ff", "acaf", "390c", "1a9b", "e7e2", "a35c", "fafd", "b759", "5eba", "6506", "d5ce", "2df5", "476b", "ca78", "8797", "821c", "28e7", "2bcb", "7906", "6c2a", "734e", "ad9a", "7acd", "6c65", "8d90", "6c81", "b3a8", "bfac", "d96e", "8d45", "b365", "2bf7", "bec9", "25c8", "c716", "1854", "75d0", "9084", "a891", "e863", "d754", "5486", "d652", "a529", "af06", "2b97", "3e5c", "6c7d", "9d26", "5db7", "69cc", "e304", "94cf", "e7c9", "67c7", "df95", "8858", "9319", "b91e", "1ff8", "ed2e", "9628", "70ba", "2ea8", "a5d8", "d59b", "a0c6", "2f25", "f7ba", "db04", "c53f", "e2f7", "bf10", "1392", "ff42", "31d4", "edab", "5bea", "dd25", "32e6", "980e", "8286", "23e8", "4379", "88cc", "de9a", "92dd", "4922", "7c82", "c054", "6587", "e655", "5c39", "ab8c", "29b3", "443c", "31f9", "fbff", "a08f"]

for i in pos_pw_list:
	if level_4_pw_check(i):
		break 
