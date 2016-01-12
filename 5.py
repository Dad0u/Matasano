import codecs

#s = input('Message ? ')
#key = input('Key ? ')


s = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = 'ICE'

while len(key) < len(s):
  key += key

key = key[:len(s)]

def xor(a,b):
    out = b''
    for i,j in zip(a,b):
        out += bytes([i^j])
    return out
b_s = bytes(s,'utf-8')
b_key = bytes(key,'utf-8')

b_encrypted = xor(b_s,b_key)
print(b_s,b_key,b_encrypted)

print(xor(b_key,b_encrypted))

print(codecs.encode(b_encrypted,'hex'))
