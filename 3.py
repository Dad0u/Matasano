import operator
from Tools import genkey, xor, score

s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

b = bytes.fromhex(s)
print(b)

for i in range(256):
    sc = score(xor(b,genkey(bytes([i]),len(b))))
    print(sc)

d = dict()

for i in b:
  if i in d.keys():
    d[i]+=1
  else:
    d[i]=1



sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
print(sorted_d)
