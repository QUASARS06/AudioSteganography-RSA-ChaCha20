import wave
import rsa_encryption
from base64 import b64encode, b64decode
import random, quantumrandom, sys
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

image_true = True

# Read the Song Input
song = wave.open("./sample.wav", mode='rb')


# Read frames and convert the audio into a byte array
frame_bytes = bytearray(list(song.readframes(song.getnframes())))


# Secret message which is to be hidden
# string='Do you really listen when you are talking with someone? I have a friend who listens in an unforgiving way. She actually takes every word you say as being something important and when you have a friend that listens like that, words take on a whole new meaning.'
string = ''

#  | 1,3 - jpg | 2 - png
image_name = 'image'
extension = 'jpg'
if image_true:
	with open(image_name+'.'+extension, "rb") as image:
		string = b64encode(image.read()).decode('utf-8')


# ChaCha20 Encryption
key = quantumrandom.binary()[:32]	# 32 byte(character) BINARY string which is required by the ChaCha20 Algorithm - Used as a key
# key = get_random_bytes(32)
# There is a method called get_random_bytes(32) in-built which can do the same thing


# Create a new ChaCha20 cipher
cipher = ChaCha20.new(key=key)


# The above cipher produces a NONCE
nonce = b64encode(cipher.nonce).decode('utf-8')


# Encrypt our Secret text using the above generated Cipher
ciphertext = cipher.encrypt(string.encode())


# Encoding the ciphertext generated above
ct = b64encode(ciphertext).decode('utf-8')


# Now we convert the above generated cipher text to binary so as to store it into our frames of audio
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in ct])))

# Stroing the length of the BITS in l1
l1 = len(bits)
print('bits - ', l1, ' frame - ', len(frame_bytes), len(frame_bytes) >= l1)


# Shuffling Algorithm
indices = [i for i in range(0, len(frame_bytes))]
# seed = quantumrandom.get_data()[0]
seed = 453
l2 = seed
random.Random(seed).shuffle(indices)

# Replace LSB of each byte of the audio data by one bit from the text bit array
for i, bit in enumerate(bits):
    loc = indices[i]
    # print('Modified ', loc, 'th Frame Byte')
    frame_bytes[loc] = (frame_bytes[loc] & 254) | bit
    
# Get the modified bytes
frame_modified = bytes(frame_bytes)

# Write bytes to a new wave audio file
with wave.open('sample_embedded.wav', 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()


# --------------------------------------------------------------------------------------------------------------
# RSA Encryption
print('Length of Bits - ', l1, 'Seed - ', l2)


# ChaCha20 KEY + NONCE + L1 + L2
final_key = str(int.from_bytes(key, byteorder=sys.byteorder)) + "." + str(nonce) + "." + str(l1) + "." + str(l2)
public_key = rsa_encryption.importKey(open('./public.pem').read())
print('Key after merging all required parts - ', final_key)
print('Length of Key to bey encrypted - ', len(final_key.encode()))


c = rsa_encryption.encrypt(final_key.encode(), public_key) # Encrypted Cipher Text
# print(str(b64encode(c)))
c = str(b64encode(c)).lstrip("b'").rstrip("'")

f = open('encryption.txt', 'w')
f.write(str(c))
f.close()

print("Encrypted Message Saved..")