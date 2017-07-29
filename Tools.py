def xor(a,b):
    out = b''
    for i,j in zip(a,b):
        out += bytes([i^j])
    return out

def genkey(key, l):
  while len(key) < l:
    key += key
  key = key[:l]
  return key


raw_bytes = [bytes([j]) for j in range(32)] + [bytes([j]) for j in range(128,256)]
usualchar = [i for i in range(97,123)]

def score(b):
  if type(b) == type('a'):
    b = bytes(b)
  score = 0
  for i in b:
    if chr(i).lower() in 'etaoin shdrlu':
      score += 1
    elif chr(i).lower() in usualchar:
      score += .9
    elif i in raw_bytes:
      score -= 10
  return score

def hamming_dist(a,b):
  """34 µs par appel pour une longueur de 14 octets"""
  d = xor(a,b)
  out = 0
  for i in d:
    out += sum([(i>>j)%2 for j in range(0,8)])
  return out

def guessSingleXorKey(b):
  max_score = 0
  for i in range(256):
    sc = score(xor(b,genkey(bytes([i]),len(b))))
    if sc > max_score:
      max_score = sc
      key = bytes([i])
  return key

def guessXorKey(b,length):
  key = b''
  for l in range(length):
    key += guessSingleXorKey(b[l::length])
  return key

def guessKeyLength(data, maxLength = 50, samples = -1, nvalues=1):
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
  r = [i[1]+2 for i in sorted(zip(tab,range(len(tab))))]
  #if nvalues == 1:
  #  return r[0]
  #else:
  return r[:nvalues]

def pkcs7_pad(b, l = 16):
  reste = len(b)%l
  if reste == 0:
    return b
  b += bytes([l - reste])*(l-reste)
  return b

def pkcs7_unpad(b):
  l = int(b[-1])
  if b[-l:] == b[-1:]*l:
    return b[:-l]
  return b

def randomKey(l = 16):
  from random import randint
  return bytes([randint(0,255) for i in range(l)])
