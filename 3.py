from Tools import guessSingleXorKey, xor, genkey

s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

b = bytes.fromhex(s)

key = guessSingleXorKey(b)

print(key)
print(xor(b,genkey(key,len(b))))