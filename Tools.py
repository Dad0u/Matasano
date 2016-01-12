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
  for i in b:
    if chr(i).lower() in 'etaoin shdrlu':
      score += 1
    elif chr(i).lower() in [i for i in range(97,123)]:
      score += .9
    elif i in [bytes([j]) for j in range(32)]:
      score -= 5
  return score
  
def guessSingleXorKey(b):
  max_score = 0
  for i in range(256):
    sc = score(xor(b,genkey(bytes([i]),len(b))))
    if sc > max_score:
      max_score = sc
      key = bytes([i])
  return key