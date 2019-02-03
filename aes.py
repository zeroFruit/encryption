from Crypto.Cipher import AES
from Crypto import Random
import binascii

# we can use the AES algorithm like this
# there are several modes (7 modes)
# 1.) ECB: "Electronic Code Book" -> we use AES on every 128 bits long plaintext block
#           these blocks are independent of each other so we use AES separately on every block
# 2.) CBC: "Cipher Block Chain" -> uses a chaining mechanism that causes
#           the decryption of a block of ciphertext to depend on all the preceding ciphertext blocks
# 
# THE PADDING PROBLEM
#   AES algorithm uses 128 bits long input: what is the plaintext is not divisible by 128?
#       - in these cases we append some extra bits to the plaintext to be able to split
#           the plaintext into 64 bits long chunks
#
#   PADDING MODES:
#       - we can add extra bits: 10000 for example
#       - we can add white-spaces to the plaintext
#       - we can use CMS "Cryptographic Message Syntax" ... pad with bytes all of the same value as the number of padding styles  
#

def append_space_padding(str, blocksize=128):
    pad_len = blocksize - (len(str) % blocksize)
    padding = 'a'*pad_len
    return str + padding

def remove_space_padding(str, blocksize=128):
    pad_len = 0

    for char in str[::-1]:
        if char == 'a':
            pad_len += 1
        else:
            break
    
    return str[:-pad_len]

def encrypt(plaintext, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(plaintext)

def decrypt(ciphertext, key):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.decrypt(ciphertext).decode('UTF-8')

if __name__ == "__main__":
    # key is 128 bits - 16 bytes
    key = Random.new().read(16)

    print("key: %s" % key.encode('hex'))

    plaintext = "This is the secret message we want to encrypt"

    print("length of plaintext: %d" % len(plaintext))
    print("plaintext: %s" % plaintext)

    paddedtext = append_space_padding(plaintext)

    print("length of paddedtext: %d" % len(paddedtext))
    print("paddedtext: %s" % paddedtext)

    ciphertext = encrypt(paddedtext, key)

    print("hexified ciphertext: %s" % binascii.hexlify(bytearray(ciphertext)))

    decrypted = decrypt(ciphertext, key)
    maybe_plaintext = remove_space_padding(decrypted)
    
    print("decrypted text: %s" % maybe_plaintext)