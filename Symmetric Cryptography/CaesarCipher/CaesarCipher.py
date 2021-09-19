import string

def CaesarCipher(text, z):
    z = z%26
    alphabet_low = list(string.ascii_lowercase)
    alphabet_up = list(string.ascii_uppercase) 
    plaintext = (list(text))
    for i in range(len(plaintext)):
        if plaintext[i] in alphabet_low:
            indexval = alphabet_low.index(plaintext[i])
            shift = indexval + z
            shift = shift%26
            plaintext[i] = alphabet_low[shift]
        elif plaintext[i] in alphabet_up:
            indexval = alphabet_up.index(plaintext[i])
            shift = indexval + z
            shift = shift%26
            plaintext[i] = alphabet_up[shift]
    ciphertext = ''.join(map(str, plaintext))
    return ciphertext

def CaesarDecipher(text, z):
    z2 = -z
    print(z2)
    CaesarCipher(text, z2)

# CaesarDecipher("QNGWFWD", 5)
print(CaesarCipher("MEETMELATER", 23))
print(CaesarCipher("EAMEELTTMER", 23))
