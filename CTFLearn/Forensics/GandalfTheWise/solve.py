import base64

s1 = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
s2 = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"
s1_decode = base64.b64decode(s1)
s2_decode = base64.b64decode(s2)
print("string s1:", s1_decode)
print("string s2:", s2_decode)
s3 = "". join([chr(a ^ b) for a,b in zip(s1_decode, s2_decode)])
print("flag:",s3)
