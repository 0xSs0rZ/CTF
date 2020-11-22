#!/usr/bin/python3

# JISCTF 2020 Quals - Ransomware chall

import base64

with open("flag.enc", "rb") as cipher:
    c = cipher.read()
    
plaintext = base64.b64decode(c)

while 'jisctf' not in str(plaintext):
    plaintext = base64.b64decode(plaintext)
    #print(plaintext)
    # Extraction du PNG trouvé
    if '\\n\\rGNP' in str(plaintext):
        print('writing png')
        f=open("test","wb")
        f.write(plaintext)
        f.close()
