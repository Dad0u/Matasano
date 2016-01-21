from Crypto.Cipher import AES
from Tools import pkcs7_pad
from Base64 import bytesFromBase64,toBase64

key = bytes([45,72,2,149,213,5,43,78,230,109,54,18,138,243,83,128])

class AES_ECB():

  def __init__(self, key):
    self.cipher = AES.AESCipher(key,AES.MODE_ECB)
    self.unknown = bytesFromBase64("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")

  def encrypt(self, data):
    data = pkcs7_pad(data+self.unknown)
    return self.cipher.encrypt(data)

def guessBlockSize(encrypt):
  size = 2
  prev = encrypt(bytes(2))[:2]
  while size < 20:
    size += 1
    enc = encrypt(bytes(size))[:size+1]
    if prev[:-1] == enc[:-2]:
      #print("stop")
      break
    #print(enc[:-1])
    #print(len(enc[:-1]),len(prev))
    #print(prev)
    prev = enc
  return size-1
    

ecb = AES_ECB(key)
print(guessBlockSize(ecb.encrypt))
