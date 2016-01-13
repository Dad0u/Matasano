from Base64 import bytesFromBase64

key = 'YELLOW SUBMARINE'

with open('7.txt','r') as f:
  f_b64 = ''.join(f.read().split("\n"))
f_b = bytesFromBase64(f_b64)

print(f_b)