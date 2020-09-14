from pwn import *

#Ref: https://github.com/JesseEmond/matasano-cryptopals/blob/master/src/aes.py
#Ref: https://raywang.tech/2017/03/07/set2_writeup/

def get_blocks(bytes_, blocksize=16):
    return [bytes_[i:i+blocksize] for i in range(0, len(bytes_), blocksize)]
    
def cbc_or_ecb(rep):
	cipher = str(rep)
	cipher = cipher.replace('Ciphertext is:  ','')
	cipher = cipher.replace('ECB or CBC?','')
	#print cipher
	#Ref: https://github.com/JesseEmond/matasano-cryptopals/blob/master/src/set_2/11.py

	blocks = get_blocks(str.encode(cipher))

	unique_blocks = len(set(blocks))

	guess = "ECB" if unique_blocks != len(blocks) else "CBC"

	#print guess
	return guess

def send_payload():
    payload = 'A'*199
    r.sendline(payload)
    rep = r.recv()
    print rep
    print cbc_or_ecb(rep)
    r.sendline(cbc_or_ecb(rep))
    #print r.recv()
    resp = r.recv()
    print 'resp send_payload ' + resp
    #return resp

r = remote('crypto.chal.csaw.io', 5001)

print r.recv()

for i in range(200):
	print '======== Essai ' + str(i) + ' ========'
	send_payload()




