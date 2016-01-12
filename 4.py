def genkey(key,l):
  while len(key) < l:
    key += key
  return key

def xor(a,b):
    out = b''
    for i,j in zip(a,b):
        out += bytes([i^j])
    return out

def score(s):
  score = 0
  for i in s:
    if chr(i).lower() in 'etaoin shdrlu':
      score += 1
    elif chr(i).lower() in [i for i in range(97,123)]:
      score += .2
  return score

with open("4.txt",'r') as f:
  f_list = f.readlines()

bytes_list = []
for i in f_list:
  bytes_list.append(bytes.fromhex(i.strip('\n')))

length = len(bytes_list[1])


max_scores = [(0,0),(0,0),(0,0)]

for char in range(0,256):
  key = genkey(bytes([char]),length)
  for s in bytes_list:
    #print(xor(s,key))
    r = xor(s,key)
    sc = score(r)
    if sc > max_scores[2][0]:
      if sc > max_scores[1][0]:
        if sc > max_scores[0][0]:
          max_scores.insert(0,(sc,r))
        else:
          max_scores.insert(1,(sc,r))
      else:
        max_scores.insert(2,(sc,r))
      del(max_scores[3])
      print(max_scores)

print("Done!")


