## Obedient Cat

### Description

This file has a flag in plain sight (aka "in-the-clear"). [Download flag](https://mercury.picoctf.net/static/2d24d50b4ebed90c704575627f1f57b2/flag).

### Information

***Point Value***: 5 points

***Category***:  General Skills

### Hints

1. Any hints about entering a command into the Terminal (such as the next one), will start with a '$'... everything after the dollar sign will be typed (or copy and pasted) into your Terminal.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/2d24d50b4ebed90c704575627f1f57b2/flag`
3. `$ man cat`

### Solution
The challenge gives us a link to download a certain data. We can use `wget` command to download data directly from terminal. After that, we get a file named "flag". try using `cat` command to show raw content of file, also we can use `string` command to get all readable content. And then, Voila we get the flag. easy start is it?

### Flag
> picoCTF{s4n1ty_v3r1f13d_f28ac910}


## Mod 26

### Description

Cryptography can be easy, do you know what ROT13 is? `cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}`

### Information

***Point Value***: 10 points

***Category***:  Cryptography

### Hints

1. This can be solved online if you don't want to do it by hand!

### Solution

to solve this challenge i don't want to do it online but with a simple python script

#### solve.py
```
import codecs

strings = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"
print(codecs.encode(strings, 'rot_13'))

```

### Flag
> picoCTF{next_time_I'll_try_2_rounds_of_rot13_aFxtzQWR}


## Python Wrangling

### Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/ende.py) using [this password](https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/pw.txt) to get [the flag](https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/flag.txt.en)?

### Information

***Point Value***: 10 points

***Category***:  General Skills

### Hints

1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/ende.py`
2. `man python`

### Solution

Download all sources first using `wget` command. We must get the python script, encryption text and password. And then, See what python script actually does.Now we are ready to decrypt the message using the command `python ende.py -d <encrypt_file_path.txt.en>`. Last, don`t forget to insert password correctly.
> python ende.py -d flag.txt.en
> Please enter the password:6008014f6008014f6008014f6008014f

### Flag
> picoCTF{4p0110_1n_7h3_h0us3_6008014f}


## Wave a flag

### Description

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm) has extraordinarily helpful information...

### Information

***Point Value***: 10 points

***Category***:  General Skills

### Hints

1. This program will only work in the webshell or another Linux computer.
2. To get the file accessible in your shell, enter the following in the Terminal prompt: `$ wget https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm`
3. Run this program by entering the following in the Terminal prompt: `$ ./warm`, but you'll first have to make it executable with `$ chmod +x warm`
4. -h and --help are the most common arguments to give to programs to get more information from them!
5. Not every program implements help features like -h and --help.

### Solution

we have an ELF file. Try to run this, but change the access permission first with `chmod +x` to make file executable
> chmod +x warm\
> ./warm

output:
> Hello user! Pass me a -h to learn what I can do!

Try to add more arguments with pass an "-h" to the program
> ./warm -h


### Flag
> picoCTF{b1scu1ts_4nd_gr4vy_d6969390}


## information

### Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](https://mercury.picoctf.net/static/c28a959c5605d5f67480d5dd3a77f302/cat.jpg)

### Information

***Point Value***: 10 points

***Category***:  Forensics

### Hints

1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}

### Solution

The hint is "look at the detail of the file", so lets try to look deeper at the file, yeap we are going through metadata of file. We need the tools called exiftool. type "exiftool cat.jpg" on the terminal. 
> exiftool cat.jpg

```
ExifTool Version Number         : 12.41
File Name                       : cat.jpg
Directory                       : .
File Size                       : 858 KiB
File Modification Date/Time     : 2021:03:16 01:24:46+07:00
File Access Date/Time           : 2022:07:12 08:41:46+07:00
File Inode Change Date/Time     : 2022:07:12 08:41:46+07:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

In here we got a bunch of information. If we focus on the "License" i think it is a string encrypt with base64. So lets decrypt it. We have to use `grep` and `sed` command to catch the string and base64 decode to decrypt the string, or the easiest way is copy and paste that string lmao. Without a further ado, type this command on the terminal `exiftool cat.jpg | grep 'License' | sed 's/.*: //' | base64 -d`

> exiftool cat.jpg | grep 'License'
```
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```
> exiftool cat.jpg | grep 'License' | sed 's/.*: //'
```
cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```
Now we got a string. Time to decrypt
> exiftool cat.jpg | grep 'License' | sed 's/.*: //' | base64 -d

### Flag
> picoCTF{the_m3tadata_1s_modified}


## Nice netcat...

### Description

There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22342`, but it doesn't speak English...

### Information

***Point Value***: 15 points

***Category***:  General Skills

### Hints

1. You can practice using `netcat` with this picoGym problem: [what's a netcat?](https://play.picoctf.org/practice/challenge/34)
2. You can practice reading and writing ASCII with this picoGym problem: [Let's Warm Up](https://play.picoctf.org/practice/challenge/22)

### Solution

If we run nc from the terminal, the output is only number. I think its a decimal number from ascii. Therefore, we need to convert that decimal to char. In this situation we can use `awk` command. Try to run this: 
> nc mercury.picoctf.net 22342 | awk '{printf "%c",$1}'

### Flag
> picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}


## Transformation

### Description

I wonder what this really is... [enc](https://mercury.picoctf.net/static/e47483f88b12f2ab0c46315afc12f64d/enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

### Information

***Point Value***: 20 points

***Category***:  Reverse Engineering

### Hints

1. You may find some decoders online

### Solution

The challenge gives us encryption algorithm, and encrypted text. So we can get the flag by reversing that algorithm. I have created a simple python script to solve this challenge. Run this script:

#### solve.py
```
encrypted_text = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽'
for i in encrypted_text:
    i = ord(i)
    belakang = str(bin(i)[-7:])
    print(f"{chr(i>>8)}{chr(int(belakang,2))}",end='')
```

### Flag
> picoCTF{16_bits_inst34d_of_8_e141a0f7}


## Stonks

### Description

I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/f9d545499faf6f436853685ad21dcb33/vuln.c) `nc mercury.picoctf.net 33411`

### Information

***Point Value***: 20 points

***Category***:  Binary Exploitation

### Hints

1. Okay, maybe I'd believe you if you find my API key.

### Solution

 The Vulnerability of this program is on the statement below.  
 ```
 scanf("%300s", user_buf);
 printf(user_buf);
 ```
 
We can figure out the system data with input user. Try to put this string `"%x%x%x%x%x%x%x"` in input (length of the string is what you want). he output will contain a hex digit which might be a flag. I have been make an input in "input" file (we only use fitur 1 [buy some stonks] because the vuln command is on that).

> nc mercury.picoctf.net 33411\
> 1\
> %x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x

And we got this:
> 8271410804b00080489c3f7f14d80ffffffff1826f160f7f22110f7f14dc708270180882713f082714106f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6334326136613431fff7007df7f4faf8

We can easily convert that in [online converter](https://www.rapidtables.com/convert/number/hex-to-ascii.html)
> ocip{FTC0l_I4_t5m_ll0m_y_y3nc42a6a41ÿ£}

after a few seconds we've got the flag, but not done here. It's looks like a little endian so we have to reverse every 4 digits with [python script](https://github.com/snykk/CTF-WriteUps/blob/master/PicoCTF/Binary%20Exploitation/Stonks/reverse.py)  for a tiny automation

### Flag
> picoCTF{I_l05t_4ll_my_m0n3y_a24c14a6}


## GET aHEAD

### Description

Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:15931/](http://mercury.picoctf.net:15931/)

### Information

***Point Value***: 20 points

***Category***:  Web Exploitation

### Hints

1. Maybe you have more than 2 choices
2. Check out tools like Burpsuite to modify your requests and look at the responses

### Solution
We can use the burpsuite suite to handle and manipulate requests. change "GET" method to "HEAD" and we can see the difference in response

### Flag
> picoCTF{r3j3ct_th3_du4l1ty_82880908}


## Mind your Ps and Qs

### Description

In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/12d820e355a7775a2c9129b2622a7eb6/values)

### Information

***Point Value***: 20 points

***Category***:  Cryptography

### Hints
1. Bits are expensive, I used only a little bit over 100 to save money

### Solution
RSA is all about crazy big prime factorization. If you new for this try to learn more about what [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) is. Here summary of the RSA theorem:

- C = Ciphertext
- M = Message (plain text)
- p and q = big prime numbers
- n = p * q
- phi = (p-1) * (q-1)
- e = some number that 1 < e < phi and gcd(e,phi) == 1 
- e * d = 1 mod phi and 0 <= d <= n
- C = M^e mod , where 0 <= M < N (for encryption)
- M = C^d mod n (for decryption)

Run this [script](https://github.com/snykk/CTF-WriteUps/blob/master/PicoCTF/Cryptography/Mind%20Your%20Ps%20and%20Qs/solve.py) to get the flag

```

from Crypto.Util.number import inverse, long_to_bytes

c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e = 65537
p = 2159947535959146091116171018558446546179
q = 658558036833541874645521278345168572231473

phi = (p-1)*(q-1)

d = inverse(e, phi)

m = pow(c,d,n)

print(long_to_bytes(m))
```

### Flag
> picoCTF{sma11_N_n0_g0od_00264570}


## Static ain't always noise

### Description

Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/static)? This [BASH script](https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/ltdis.sh) might help!

### Information

***Point Value***: 20 points

***Category***:  General Skills

### Hints
no hint

### Solution
We can use the `strings` command to get all the readable content of the [ELF file](https://github.com/snykk/CTF-WriteUps/tree/master/PicoCTF/General%20Skills/Static%20aint%20always%20noise). Add grep with pipe to get specific content using pico ctf flag pattern
> strings static | grep pico

### Flag
> picoCTF{d15a5m_t34s3r_98d35619}


## Tab, Tab, Attack

### Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/e38f6a5b69b45d21e33cf7281d8c2531/Addadshashanammu.zip)

### Information

***Point Value***: 20 points

***Category***:  General Skills

### Hints
1. After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

### Solution
Extract the zip file first. And then use the `cd` command and tab power to go deeper until we find an ELF file. Run to get the flag

### Flag
> picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}


## keygenme-py

### Description

[keygenme-trial.py](https://mercury.picoctf.net/static/fb75b48f9214cf992a2199b5785564e7/keygenme-trial.py)

### Information

***Point Value***: 30 points

***Category***:  Reverse Engineering

### Hints
no hint

### Solution
#### looking at the source code
sometimes the best way to solve a reverse engineering challenge is to look at the [source code](https://github.com/snykk/CTF-WriteUps/blob/master/PicoCTF/Reverse%20Engineering/Keygenme-py/keygenme-trial.py), right?
```
# GLOBALS --v
arcane_loop_trial = True
jump_into_full = False
full_version_code = ""

username_trial = "FREEMAN"
bUsername_trial = b"FREEMAN"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

What is really important to us?
```
username_trial = "FREEMAN"
bUsername_trial = b"FREEMAN"
```
This will become clear later, next of course flags! Or here it is called **key_full_template_trial** . It consists of two parts static, and  a dynamic part.
```
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
Good... Now we have to look how the dynamic part is generated

#### dynamic key generated

**check_key** function is used to check dynamic key validity
```
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False

        return True
```
First, check if the entered keys are the same length. also checks if the entered static key has the same characters. Next, the iterator `i` is in our dynamic section, and the `if tree` that checks our dynamic keys. you notice something? yeap, we have many indexes {4,5,3,6,2,7,1,8}. This index is used to retrieve certain characters from the sha256 hashing based on `username_trial` "FREEMAN" we saw earlier. Now we just need to create a script to retrieve certain characters  from the sha256 hash based on the index we got earlier. This is pretty easy to script. 
[solve.py](https://github.com/snykk/CTF-WriteUps/blob/master/PicoCTF/Reverse%20Engineering/Keygenme-py/solve.py)
```
import hashlib
from cryptography.fernet import Fernet
import base64
import sys

username_trial = "FREEMAN"
a = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()
print(f"{a[4]}{a[5]}{a[3]}{a[6]}{a[2]}{a[7]}{a[1]}{a[8]}")
```
> 0d208392

Now we got the flag, just replace that string into our dynamic part
### Flag
> picoCTF{1n_7h3_|<3y_of_0d208392}


## Matryoshka doll

### Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/205adad23bf9d8303081a0e71c9beab8/dolls.jpg)

### Information

***Point Value***: 30 points

***Category***:  Forensics

### Hints
1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as picoCTF{XXXXX}

### Solution
The challenge give us a link to download the image file. At first this image looks useless. But, remember this is a forensic challenge. We have to look deeper into the file. I think there is a file inside this image, maybe rar or something. We can use powerful tool named [binwalk](https://www.kali.org/tools/binwalk/) to extract rar inside image easily with `binwalk e <name_file>`. 
```
Binwalk v2.3.3
Craig Heffner, ReFirmLabs
https://github.com/ReFirmLabs/binwalk

Usage: binwalk [OPTIONS] [FILE1] [FILE2] [FILE3] ...

Signature Scan Options:
    -B, --signature              Scan target file(s) for common file signatures
    -R, --raw=<str>              Scan target file(s) for the specified sequence of bytes
    -A, --opcodes                Scan target file(s) for common executable opcode signatures
    -m, --magic=<file>           Specify a custom magic file to use
    -b, --dumb                   Disable smart signature keywords
    -I, --invalid                Show results marked as invalid
    -x, --exclude=<str>          Exclude results that match <str>
    -y, --include=<str>          Only show results that match <str>
    
Extraction Options:
    -e, --extract                Automatically extract known file types
    -D, --dd=<type[:ext[:cmd]]>  Extract <type> signatures (regular expression), give the files an extension of <ext>, and execute <cmd>
    -M, --matryoshka             Recursively scan extracted files
....
```
Extract image
```
┌──(fikri㉿rootKali)-[~/Documents/Github/CTF-WriteUps/PicoCTF/Forensics/Matryoshka doll]
└─$ binwalk -e dolls.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378952, uncompressed size: 383937, name: base_images/2_c.jpg
651610        0x9F15A         End of Zip archive, footer length: 22
```

At the first time, we get a folder ending with the name `.extracted`. we must enter it with the command `cd`. there is also a folder `base image` we have to go into it too. here we get another image file with the name `2_c.jpg`. Use [binwalk](https://www.kali.org/tools/binwalk/) again to extract the rar inside the image. Repeat this step until you get the flag.txt file. This is what my terminal looks like
> binwalk -e dolls.jpg\
> cd _dolls.jpg.extracted/\
> cd base_images/\
> binwalk -e 2_c.jpg\
> cd _2_c.jpg.extracted/\
> cd base_images/\
> binwalk -e 3_c.jpg\
> cd _3_c.jpg.extracted/\
> cd base_images/\
> binwalk -e 4_c.jpg\
> cd _4_c.jpg.extracted/\
> cat flag.txt

### Flag
> picoCTF{96fac089316e094d41ea046900197662}

