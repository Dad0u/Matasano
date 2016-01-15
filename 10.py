from Crypto.Cipher import AES
from Tools import xor

class AES_CBC():
  def __init__(self, key):
    self.cipher = AES.AESCipher(key,AES.MODE_ECB)
    self.iv = bytes(16)

  def encrypt(self, data):
    enc = self.iv
    out = b''
    if len(data)%16 != 0:
      data += bytes(16-len(data)%16)
    for i in range(len(data)//16):
      block = data[16*i:16*(i+1)]
      block = xor(block,enc)
      enc = self.cipher.encrypt(block)
      out += enc
    if len(data)%16 == 0:
      return out
      

  def decrypt(self, data):
    out = b''
    enc = bytes(len(data))
    prev = self.iv
    for i in range(len(data)//16):
      block = data[16*i:16*(i+1)]
      dec = xor(self.cipher.decrypt(block),prev)
      out += dec
      prev = block
    return out.rstrip(bytes(1))

data = b''
with open('10.txt', 'r') as f:
  data = bytes(f.read().strip('\n'),"utf-8")

cbc = AES_CBC('YELLOW SUBMARINE')

enc = cbc.encrypt(data)

print(cbc.decrypt(enc))
