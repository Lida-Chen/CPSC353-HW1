# Author: Danni Du
import random
import string

# create and print the key
def CreateKey():
    # for CaesarCipher, key should be A-' ', they represent to 0-26
    key = random.randint(0,26)
    print(f"this is the key for Caesar Cipher : {chr(ord('A') + key)}")
    return key

# print the encrypted strings and how you get it
def encrypt(letters):
    encrypt_text = ""
    key = CreateKey()               # create key randomly
    Letter = "A"
    Letternum = 0
    Encryptletter = "A"
    Encryptnum = 0
    for l in letters:
        if l == " ":                # if letters contains " ", let number = 26 then process encrypt
            Letternum = 26
            Encryptnum = (Letternum + key) % 27
            if Encryptnum == 26:
                Encryptletter = " "
            else:
                Encryptnum += ord(Letter)
                Encryptletter = chr(Encryptnum)    
        else:
            Encryptnum = (ord(l) - ord(Letter) + key) % 27   # let letter number equal to the specified number then process encrypt
            if Encryptnum == 26:
                Encryptletter = " "
            else:
                Encryptnum += ord(Letter)
                Encryptletter = chr(Encryptnum) 
        encrypt_text = encrypt_text + Encryptletter
        # output the process
        print(f"{l}({ord(l) - ord(Letter)}) + {key} = {Encryptletter}({Encryptnum-ord(Letter)})")
    # output the final result
    print(f"Encrypted letters: {encrypt_text}")
    return encrypt_text
        


# print the decrypted strings and how you get it
# check if the key is legal
def decrypt(letters, realkey):
    # check whether key is a letter or space or not
    if not realkey.isalpha() or len(realkey) != 1:
        if not realkey == " ":
            print("Please choose a single character from 'A' to 'Z' or 'a' to 'z' or space")
            quit()
    decrypt_text = ""
    Letter = "A"
    # let key equal to specified numbers
    if realkey == " ":
        key = 26
    else:
        key = ord(realkey) - ord(Letter)
    for l in letters:
        # let letters equal to specified numbers
        if l == " ":       
            Letternum = 26
        else:
            Letternum = ord(l) - ord(Letter)
        # decrypt
        Decryptnum = (Letternum - key) % 27
        if Decryptnum == 26:
            Decryptletter = " "
        else:
            Decryptletter = chr(Decryptnum + ord(Letter))
        decrypt_text += Decryptletter
        # print process
        print(f"{l}({Letternum}) - {realkey}({key}) = {Decryptletter}({Decryptnum})") 
    # print result   
    print(f"Decrypted letters: {decrypt_text}")
    return decrypt_text

               
               

