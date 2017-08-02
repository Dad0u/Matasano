from Crypto.Cipher import AES
from Tools import random_bytes,pkcs7_pad
from random import randint

class RandomEncryption():
  def __init__(self):
    self.mode = "ECB" if randint(0,1) else "CBC"
    if self.mode == "CBC":
      args = [random_bytes(16),AES.MODE_CBC,random_bytes(16)]
    else:
      args = [random_bytes(16),AES.MODE_ECB]
    self.cipher = AES.AESCipher(*args)

  def encrypt(self,data):
    data = random_bytes(randint(5,10))+data+random_bytes(randint(5,10))
    return self.cipher.encrypt(pkcs7_pad(data))

def is_ecb(cipher,bs=16):
  data = cipher.encrypt(bytes([97]*(bs*3)))
  blocks = [data[i:i+bs] for i in range(0,len(data),bs)]
  return len(set(blocks)) != len(blocks)

for i in range(50):
  c = RandomEncryption()
  if is_ecb(c):
    assert c.mode == "ECB"
  else:
    assert c.mode == "CBC"

print("Success!")
