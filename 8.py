from Crypto.Cipher import AES

with open('8.txt','r') as f:
  f_b64 = f.read().split("\n")
f_b = []
for i in f_b64:
  f_b.append(bytes.fromhex((i)))

#print(len(f_b[0]))

for data in f_b:
  for i in range(len(data)//16 - 1):
    if data[i*16:16*(i+1)] == data[(i+1)*16:(i+2)*16]:
      print(data)
#cipher = AES.AESCipher(key)
