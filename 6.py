from Base64 import bytesFromBase64, toBase64

def xor(a,b):
    out = b''
    for i,j in zip(a,b):
        out += bytes([i^j])
    return out
    
def genkey(key,l):
  while len(key) < l:
    key += key
  return key

def hamming_dist(a,b):
  """34 µs par appel pour une longueur de 14 octets"""
  d = xor(a,b)
  out = 0
  for i in d:
    out += sum([(i>>j)%2 for j in range(0,8)])
  return out
  
def gessKeyLength(data, maxLength = 50, samples = 4):
  tab = []
  for keysize in range(2,maxLength):
    hd = []
    for sample in range(1,samples):
      hd.append(hamming_dist(data[(sample-1)*keysize:sample*keysize],data[sample*keysize:(sample+1)*keysize]))
    tab.append(sum(hd)/samples/keysize)
  print(tab)
  return 2+tab.index(max(tab))
  
  
def guessSingleXorKey(data):
  def score(s):
    score = 0
    for i in s:
      if chr(i).lower() in 'etaoin shdrlu':
        score += 1
      elif chr(i).lower() in [i for i in range(97,123)]:
        score += .9
      elif chr(i) in [i for i in range(0,32)]:
        score -=3
    return score
  
  
  max_score = 0
  for char in range(0,256):
    key = genkey(bytes([char]),len(data))
    sc = score(xor(data,key))
    if sc > max_score:
      result = char
      max_score = sc
  return result
  
f = open('6.txt','r')
c_f = "".join(f.read().split("\n"))

data = bytesFromBase64(c_f)

#data = bytes.fromhex('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f')

length = gessKeyLength(data)
#length = 12

print("Longueur de la clé: "+str(length))


"""
hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
data = bytes.fromhex(hex)

key = chr(guessSingleXorKey(data))
print(key)


print(xor(bytes(genkey(key,len(data)),'utf-8'),data))
"""

for length in range(2,30):
    key = ''
    for l in range(length):
      c = chr(guessSingleXorKey(data[l::length]))
      print(c)
      key += c
    print(key)
    print(xor(bytes(genkey(key,len(data)),'utf-8'),data))

