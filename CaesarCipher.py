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
            Encryptnum = (Letternum + key) % 27
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
        print(f"{l}({ord(l) - ord(Letter)}) + {key} = {Encryptletter}({Encryptnum-ord(Letter)})")
    print(f"Encrypted letters: {encrypt_text}")
    return encrypt_text
        


# print the decrypted strings and how you get it
# check if the key is legal
def decrypt(letters, realkey):
    if not realkey.isalpha() or len(realkey) != 1:
        print("Please choose a single character from 'A' to 'Z' or 'a' to 'z'")
        quit()
    decrypt_text = ""
    Letter = "A"
    key = ord(realkey) - ord(Letter)
    for l in letters:
        if l == " ":
            Letternum = 26
        else:
            Letternum = ord(l) - ord(Letter)
        Decryptnum = (Letternum - key) % 27
        if Decryptnum == 26:
            Decryptletter = " "
        else:
            Decryptletter = chr(Decryptnum + ord(Letter))
        decrypt_text += Decryptletter
        print(f"{l}({Letternum}) - {realkey}({key}) = {Decryptletter}({Decryptnum})")    
    print(f"Decrypted letters: {decrypt_text}")
    return decrypt_text

               
               

