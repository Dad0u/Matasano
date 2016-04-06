from Crypto.Cipher import AES
from Tools import randomKey, pkcs7_pad, pkcs7_unpad

class Oracle():

  def __init__(self, key):
    self.cipher = AES.AESCipher(key,AES.MODE_ECB)
    self.before = b'email='
    self.after = b'&uid=10&role=user'

  def encrypt(self, data):
    data = pkcs7_pad(data)
    return self.cipher.encrypt(data)

  def decrypt(self, data):
    return pkcs7_unpad(self.cipher.decrypt(data))

  def parse(self,s):
    l = s.split('&')
    d = dict()  
    for i in l:
      i = i.split('=')
      d[i[0]] = i[1]
    return d

  def profile_for(self,s):
    def strip(c,s):
      while c in s:
        pos = s.find(c)
        s = s[:pos]+s[pos+1:]
      return s

    s = strip("=",s)
    s = strip("&",s)
    s = bytes(s,'utf-8')    
    s = self.before + s + self.after
    
    return self.encrypt(s)

def findChar(encrypt, feed, goal, size):
  for i in range(256):
    if encrypt(feed+bytes([i]))[:size] == goal:
      return bytes([i])
  #print('FAILED !')

def decompose(s):
  if type(s) == type('foo'):
    s = bytes(s,'utf-8')
  out = b''
  for i in range(len(s)//16):
    out += s[16*i:16*(i+1)]+b'|'
  if len(s) % 16 != 0:
    out += s[-(len(s) % 16):]
  return out


key = randomKey()
oracle = Oracle(key)

profile = oracle.profile_for('foooo@bar.com')
admin = oracle.profile_for('aaaaaaaaaaadmin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b')[16:32]
print(admin)
#print(oracle.decrypt(admin))

profile = profile[:32]+admin


#--------------------------------------------
d = oracle.decrypt(profile)


print(d)
