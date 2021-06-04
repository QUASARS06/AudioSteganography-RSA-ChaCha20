import wave, random, sys
from base64 import b64encode, b64decode
from Crypto.Cipher import ChaCha20
from rsa_decryption import get_keys

image_true = True
ext = '.jpg'
song = wave.open("sample_embedded.wav", mode='rb')
# Convert audio to byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))


keys = get_keys().split('.')
# print(keys)

chacha20_key = int(keys[0]).to_bytes(32, byteorder=sys.byteorder)
nonce = keys[1]
l1 = int(keys[2])
l2 = int(keys[3])
print(l1, l2)


indices = [i for i in range(0, len(frame_bytes))]
random.Random(l2).shuffle(indices)


extracted = []
for i in range(0, l1):
    loc = indices[i]
    extracted.append(frame_bytes[loc] & 1)

# Extract the LSB of each byte
# extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# Convert byte array back to string
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
# Cut off at the filler characters
# decoded = string.split("###")[0]
# print(string)


try:
	nonce = b64decode(nonce)
	ciphertext = b64decode(string)
	cipher = ChaCha20.new(key=chacha20_key, nonce=nonce)
	plaintext = cipher.decrypt(ciphertext)

	if image_true:
		decodeit = open('decoded_image'+ext, 'wb') 
		decodeit.write(b64decode(plaintext.decode().encode('utf-8'))) 
		decodeit.close()
	else:
		print("The message was - ", plaintext.decode())
		
except ValueError:
	print("Incorrect decryption")

song.close()