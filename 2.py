import codecs

s_a = '1c0111001f010100061a024b53535009181c'

s_b = '686974207468652062756c6c277320657965'

a = bytes.fromhex(s_a)
b = bytes.fromhex(s_b)

def xor(a,b):
    out = b''
    for i,j in zip(a,b):
        out += bytes([i^j])
    return out

print(codecs.encode(xor(a,b),'hex'))
