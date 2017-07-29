import codecs

#s = input('Message ? ')
#key = input('Key ? ')
from Tools import genkey,xor


s = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

key = genkey('ICE',len(s))

b_s = bytes(s,'utf-8')
b_key = bytes(key,'utf-8')

b_encrypted = xor(b_s,b_key)
print(b_s,b_key,b_encrypted)

print(xor(b_key,b_encrypted))

print(codecs.encode(b_encrypted,'hex'))
