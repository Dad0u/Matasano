from Base64 import bytesFromBase64
from Crypto.Cipher import AES

key = b'YELLOW SUBMARINE'

with open('7.txt','r') as f:
  f_b64 = ''.join(f.read().split("\n"))
f_b = bytesFromBase64(f_b64)

cipher = AES.AESCipher(key)

print(cipher.decrypt(f_b))
