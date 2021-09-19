"""
Let's now use a modified Caesar Cipher where:
      c = (p+3x) mod 26,
where c and p are the ciphertext and the plaintext, respectively, and x is the key.
How many distinct keys, producing distinct encryption/decryption transformations, are there now?
"""

def how_many_distinct_keys(multip, Z):
    """c = ( p + (multip)*x ) mod Z
    How many distinct keys, producing distinct encryption/decryption transformations,
    are there now?
    example: c = (p+3*x) mod 26"""
    class_mod=[]
    for i in range(Z):
        k=((i*multip)%Z)
        class_mod.append(k)
    print("the set of class are: ", list(set(class_mod)))
    print("There are", len(list(set(class_mod))), "different keys")

how_many_distinct_keys(3,26)