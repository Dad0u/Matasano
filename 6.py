from Base64 import bytesFromBase64
from Tools import *


f = open('6.txt','r')
c_f = "".join(f.read().split("\n"))

data = bytesFromBase64(c_f)
#text = "Bonjour, ceci est un petit test pour vérifier le crack du "\
#    "chiffrement single-Byte XOR avec une chaine encodée en UTF-8 :)\n"\
#    "J'ai malgré tout l'impression qu'il faut une chaine suffisamment "\
#    "longue pour lisser les irrégularités dûes à l'utilisation de la "\
#    "distance de Hamming entre les caractères pour la détéction de "\
#    "la longueur de la clé"
#msg = bytes(text,'utf-8')
#key = genkey(b'Wolo45pouet',len(msg))
#data = xor(key,msg)

length = guessKeyLength(data,nvalues=1)

print("Longueurs possible de la clé:",length)

keys = [guessXorKey(data,l) for l in length]

print("Possible keys and text:", [(k,xor(genkey(k,len(data)),data)) for k in keys])
