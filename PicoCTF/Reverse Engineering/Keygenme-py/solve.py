import hashlib
from cryptography.fernet import Fernet
import base64
import sys

username_trial = "FREEMAN"
a = hashlib.sha256(username_trial.encode('utf-8')).hexdigest()
print(f"{a[4]}{a[5]}{a[3]}{a[6]}{a[2]}{a[7]}{a[1]}{a[8]}")
