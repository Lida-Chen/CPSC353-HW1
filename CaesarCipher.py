# Author: Danni Du
import random
import string

# create and print the key
def CreateKey():
    # TODO
    key = random.randint(0,26)
    print(f"this is the key for Caesar Cipher : {key}")
    return key

# print the encrypted strings and how you get it
def encrypt(letters):
    # TODO
    encrypt_text = ""
    key = CreateKey()
    Letter = "A"
    Letternum = 0
    Encryptletter = "A"
    Encryptnum = 0
    letters = letters.upper()
    for l in letters:
        if l == " ":
            Letternum = 26
            Encryptnum = (26 + key) % 27
            if Encryptnum == 26:
                Encryptletter = " "
            else:
                Encryptnum += ord(Letter)
                Encryptletter = chr(Encryptnum)    
        else:
            Encryptnum = (ord(l) - ord(Letter) + key) % 27
            if Encryptnum == 26:
                Encryptletter = " "
            else:
                Encryptnum += ord(Letter)
                Encryptletter = chr(Encryptnum) 
        encrypt_text = encrypt_text + Encryptletter
    print(f"Encrypted letters: {encrypt_text}")
    return encrypt_text
        


# print the decrypted strings and how you get it
# check if the key is legal
def decrypt(letters, key):
    # TODO
    pass
