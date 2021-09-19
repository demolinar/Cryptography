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
    CaesarCipher(text, z2)

# CaesarDecipher("QNGWFWD", 5)
# CaesarCipher("LIBRARY", 5)

def VigenereCipher(text, wkey):
    alphabet_low = list(string.ascii_lowercase)
    alphabet_up = list(string.ascii_uppercase) 
    wkey = list(wkey)
    text = list(text)
    ordinal_wkey_list = []
    cipher_text_vigenere = []
    for i in range(len(wkey)):
        if wkey[i] in alphabet_low:
            ordinal_wkey_list.append(alphabet_low.index(wkey[i]))
        elif wkey[i] in alphabet_up:
            ordinal_wkey_list.append(alphabet_up.index(wkey[i]))
    for i in range(len(text)):
        if text[i] != " ":
            m = i%(len(wkey))
            cipher_text_vigenere.append(CaesarCipher(text[i],ordinal_wkey_list[m]))
        else:
            cipher_text_vigenere.append(" ")
    cipher_text_vigenere = ''.join(map(str, cipher_text_vigenere))
    print(cipher_text_vigenere)

def VigenereDecipher(text, wkey):
    alphabet_low = list(string.ascii_lowercase)
    alphabet_up = list(string.ascii_uppercase) 
    wkey = list(wkey)
    text = list(text)
    ordinal_wkey_list = []
    cipher_text_vigenere = []
    for i in range(len(wkey)):
        if wkey[i] in alphabet_low:
            ordinal_wkey_list.append(alphabet_low.index(wkey[i]))
        elif wkey[i] in alphabet_up:
            ordinal_wkey_list.append(alphabet_up.index(wkey[i]))
    print(ordinal_wkey_list)
    for i in range(len(text)):
        if text[i] != " ":
            m = i%(len(wkey))
            cipher_text_vigenere.append(CaesarCipher(text[i],-ordinal_wkey_list[m]))
        else:
            cipher_text_vigenere.append(" ")
    cipher_text_vigenere = ''.join(map(str, cipher_text_vigenere))
    return cipher_text_vigenere


# print(VigenereCipher("MEET ME LATER", "LEMON"))
print(VigenereDecipher("DTXSAOMP", "LEMON"))
# print(VigenereCipher("DRAGON", "XO"))


