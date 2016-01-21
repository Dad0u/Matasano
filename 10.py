from Crypto.Cipher import AES
from Tools import xor,pkcs7_pad,pkcs7_unpad
from Base64 import bytesFromBase64

class AES_CBC():

  def __init__(self, key, iv = bytes(16)):
    self.cipher = AES.AESCipher(key,AES.MODE_ECB)
    self.iv = iv

  def encrypt(self, data):
    enc = self.iv
    out = b''
    data = pkcs7_pad(data)
    for i in range(len(data)//16):
      block = data[16*i:16*(i+1)]
      block = xor(block,enc)
      enc = self.cipher.encrypt(block)
      out += enc
    return out

  def decrypt(self, data):
    out = b''
    enc = bytes(len(data))
    #prev = bytes(16)
    prev = self.iv
    for i in range(len(data)//16):
      block = data[16*i:16*(i+1)]
      dec = xor(self.cipher.decrypt(block),prev)
      out += dec
      prev = block
    return pkcs7_unpad(out)

"""
data = b''
with open('10a.txt', 'r') as f:
  data = bytes(f.read().strip('\n'),"utf-8")
"""

with open('10.txt','r') as f:
  data = bytesFromBase64("".join(f.read().split('\n')))
cbc = AES_CBC('YELLOW SUBMARINE')
#cbc2 = AES_CBC('YELLOW SUBMARINE', b'abcdefghijklmnop')

print(cbc.decrypt(data))



