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

