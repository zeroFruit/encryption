from Crypto.Cipher import DES
import binascii

# we can use the DES algorithm like this
# there are several modes (7 modes)
# 1.) ECB: "Electronic Code Book" -> we use DES on every 64 bits long plaintext block
#           these blocks are independent of each other so we use DES separately on every block
# 2.) CBC: "Cipher Block Chain" -> uses a chaining mechanism that causes
#           the decryption of a block of ciphertext to depend on all the preceding ciphertext blocks
# 
# THE PADDING PROBLEM
#   DES algorithm uses 64 bits long input: what is the plaintext is not divisible by 64?
#       - in these cases we append some extra bits to the plaintext to be able to split
#           the plaintext into 64 bits long chunks
#
#   PADDING MODES:
#       - we can add extra bits: 10000 for example
#       - we can add white-spaces to the plaintext
#       - we can use CMS "Cryptographic Message Syntax" ... pad with bytes all of the same value as the number of padding styles  
#

def append_space_padding(str, blocksize=64):
    pad_len = blocksize - (len(str) % blocksize)
    padding = 'a'*pad_len
    return str + padding

def remove_space_padding(str, blocksize=64):
    pad_len = 0

    for char in str[::-1]:
        if char == 'a':
            pad_len += 1
        else:
            break
    
    return str[:-pad_len]

def encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(plaintext)

def decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(ciphertext).decode('UTF-8')

if __name__ == "__main__":
    key = "secretaa"
    plaintext = "This is the secret message we want to encrypt"

    print("length of plaintext: %d" % len(plaintext))
    print("plaintext: %s" %)

    paddedtext = append_space_padding(plaintext)

    print("length of paddedtext: %d" % len(paddedtext))
    print("paddedtext: %s" % paddedtext)

    ciphertext = encrypt(paddedtext, key)

    print("hexified ciphertext: %s" % binascii.hexlify(bytearray(ciphertext)))

    decrypted = decrypt(ciphertext, key)
    maybe_plaintext = remove_space_padding(decrypted)
    
    print("decrypted text: %s" % maybe_plaintext)