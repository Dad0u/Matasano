from Base64 import bytesFromBase64, toBase64
from Tools import *

def guessKeyLength(data, maxLength = 50, samples = -1):
  if (samples+1)*maxLength > len(data):
    print('not enough data')
    return
  if samples == -1: #Échantillonne sur le maximum de données
    samples = len(data) // maxLength
  tab = []
  for keysize in range(2,maxLength):
    hd = []
    for sample in range(1,samples):
      hd.append(hamming_dist(data[(sample-1)*keysize:sample*keysize],data[sample*keysize:(sample+1)*keysize]))
    tab.append(sum(hd)/samples/keysize)
  #print(tab)
  return 2+tab.index(min(tab))

f = open('6.txt','r')
c_f = "".join(f.read().split("\n"))

data = bytesFromBase64(c_f)

length = guessKeyLength(data)

print("Longueur de la clé: "+str(length))

key = b''
for l in range(length):
  c = guessSingleXorKey(data[l::length])
  print(c)
  key += c
print(key)
print(xor(genkey(key,len(data)),data))

