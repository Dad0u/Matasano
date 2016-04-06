from Crypto.Cipher import AES
from Tools import xor,pkcs7_pad
from Base64 import bytesFromBase64
from random import randint

class RandomEncryption():

  def __init__(self, data):
    self.data = data

  def encryptCBC(self, data, key, iv):
    enc = iv
    out = b''
    cipher = AES.AESCipher(key,AES.MODE_ECB)
    for i in range(len(data)//16):
      block = data[16*i:16*(i+1)]
      block = xor(block,enc)
      enc = cipher.encrypt(block)
      out += enc
    return out

  def encryptECB(self, data, key):
    cipher = AES.AESCipher(key,AES.MODE_ECB)
    return cipher.encrypt(data)

  def genblock(self):
    data = pkcs7_pad(self.randBytes(randint(5,10)) + self.data + self.randBytes(randint(5,10)))
    print(len(data))
    c = randint(1,2)
    if c == 1:
      print('CBC')
      return self.encryptCBC(data,self.randBytes(),self.randBytes())
    else:
      print('ECB')
      return self.encryptECB(data,self.randBytes())

  def randBytes(self, n = 16):
    out = b''
    for i in range(n):
      out += bytes([randint(0,255)])
    return out

def detectEncryption(data):
  if data[16:32] == data[32:48]:
    print('ECB')
  else:
    print('CBC')

with open('10a.txt') as f:
  data = bytes(f.read(),'utf-8')
#data = bytes(64)

oracle = RandomEncryption(data)
block = oracle.genblock()
print(block)
detectEncryption(block)
