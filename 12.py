from Crypto.Cipher import AES
from Tools import pkcs7_pad, randomKey
from Base64 import bytesFromBase64,toBase64

#key = bytes([45,72,2,149,213,5,43,78,230,109,54,18,138,243,83,128])
key = randomKey()

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

def isECB(encrypt,size):
  data = encrypt(bytes(4*size))
  if data[size:2*size] == data[2*size:3*size]:
    return True
  else:
    return False

def findChar(encrypt, feed, goal, size):
  for i in range(256):
    if encrypt(feed+bytes([i]))[:size] == goal:
      return bytes([i])
  #print('FAILED !')

def guessECB(encrypt, size):
  prev = bytes(size)
  res = b''
  for i in range(len(encrypt(b''))//size): #Parcours les blocs
    curr = b''
    for j in range(size):
      goal = encrypt(prev[:size - j - 1])[i*size:(i+1)*size]
      c = findChar(encrypt, (prev+curr)[-size + 1:], goal, size)
      if c != None:
        curr += c
      #print(c)
    prev = curr
    res += curr
  return res
    

ecb = AES_ECB(key)
size = guessBlockSize(ecb.encrypt)
if not isECB(ecb.encrypt,size):
  print("Not ECB mode")
  exit(-1)

print(guessECB(ecb.encrypt,size))



