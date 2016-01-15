from Tools import pkcs7_pad, pkcs7_unpad


s = b'YELLOW SUBMARI'
padded = pkcs7_pad(s)
print(s)
print(padded)
print(pkcs7_unpad(padded))

