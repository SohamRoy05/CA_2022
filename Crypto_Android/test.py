from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib
import random
import socketserver
import signal
encrypted_sequence='00000000000000000000002b3678efbfbd753378efbfbd71d4ab3922efbfbd4065635f2befbfbd3aefbfbd25efbfbd395defbfbd2c6befbfbdefbfbdefbfbd2defbfbdefbfbdefbfbdefbfbd2eefbfbd'
encrypted_sequence = bytes.fromhex(encrypted_sequence)
print(len(encrypted_sequence))
print(b"Initialization Sequence - Code 0")
encrypted="Initialization Sequence - Code 0"

shared_secret=1
key = hashlib.md5(long_to_bytes(shared_secret)).digest()
print(key)


cipher = AES.new(key, AES.MODE_ECB)
message = cipher.encrypt(encrypted)
print(message.hex())
7fd4794e77290bf65808e95467f284966d71995c16e83da2192aecfd2d0df7a4