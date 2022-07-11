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


