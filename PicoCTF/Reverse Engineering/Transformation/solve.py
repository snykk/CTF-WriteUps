string = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽'
for i in string:
    i = ord(i)
    belakang = str(bin(i)[-7:])
    print(f"{chr(i>>8)}{chr(int(belakang,2))}",end='')