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
  
def score(b):
  if type(b) == type('a'):
    b = bytes(b)
  score = 0
  raw_bytes = [bytes([j]) for j in range(32)] + [bytes([j]) for j in range(128,256)]
  usualchar = [i for i in range(97,123)]
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