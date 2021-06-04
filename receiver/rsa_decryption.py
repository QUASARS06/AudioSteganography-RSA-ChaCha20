from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from base64 import b64decode

def decrypt(ciphertext, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   return cipher.decrypt(ciphertext)

def importKey(externKey):
   return RSA.importKey(externKey)

def get_keys():
	private_key = importKey(open('./private.pem').read())
	ciphertext = open('encryption.txt').read()
	d = decrypt(b64decode(ciphertext.encode()), private_key)
	return str(d.decode())