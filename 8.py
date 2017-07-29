from Crypto.Cipher import AES

with open('8.txt','r') as f:
  f_b64 = f.read().split("\n")
f_b = []
for i in f_b64:
  f_b.append(bytes.fromhex((i)))

for data in f_b:
  blocks = [data[i:i+16] for i in range(0,len(data),16)]
  if len(set(blocks)) != len(blocks):
    print("This one contains duplicates!",data)
