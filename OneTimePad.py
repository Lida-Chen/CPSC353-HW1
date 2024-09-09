# Author: Lida Chen
import random
import string

# create and print the key
def CreateKey(length):
    characters = string.ascii_uppercase + ' '
    key = random.choices(characters, k = length)
    print(f"Key for one time pad: {key}")
    return key

# Encrypt the message using the one-time pad cipher
# print the encrypted strings and how you get it
def encrypt(letters : str):
    key = CreateKey(len(letters)) # Generate a key of the same length as the message
    Key = "A"
    KeyNumber = 0
    Letter = "A"
    LetterNumber = 0
    EncryptedCharacter = "A"
    EncryptedNumber = 0
    EncryptedCharacters = "" # This will store the resulting encrypted message
    print("-----------------")
    # Convert the key character to a number
    for i in range(len(key)):
        if key[i] == " ":
            Key = " "
            KeyNumber = 26
        else:
            Key = key[i]
            KeyNumber = ord(key[i]) - ord('A')
        if letters[i] == " ":
            Letter = " "
            LetterNumber = 26
        else:
            Letter = letters[i]
            LetterNumber = ord(letters[i]) - ord('A')
        # Perform the encryption
        EncryptedNumber = (KeyNumber + LetterNumber) % 27
        # Convert the encrypted number back to a character
        if EncryptedNumber == 26:
            EncryptedCharacter = ' '
        else:
            EncryptedCharacter = chr(EncryptedNumber + ord('A'))
        # Print the step-by-step process of encryption
        EncryptedCharacters += EncryptedCharacter
        print(f"{Letter}({LetterNumber}) + {Key}({KeyNumber}) = {EncryptedCharacter}({EncryptedNumber})")
    print("-----------------")
    print(f"Encrypted letters: {EncryptedCharacters}")
    
    return EncryptedCharacters

# Decrypt the message using the one-time pad cipher
# print the decrypted strings and how you get it
# check if the key is legal
def decrypt(letters, key):
    if len(letters) != len(key):
        print("Key and characters have different length")
        quit()
    else:

        Key = "A"
        KeyNumber = 0
        Letter = "A"
        LetterNumber = 0
        DecryptedCharacter = "A"
        DecryptedNumber = 0
        DecryptedCharacters = ""
        # Convert the key character to a number
        for i in range(len(key)):
            if key[i] == " ":
                Key = " "
                KeyNumber = 26
            else:
                Key = key[i]
                KeyNumber = ord(key[i]) - ord('A')
            if letters[i] == " ":
                Letter = " "
                LetterNumber = 26
            else:
                Letter = letters[i]
                LetterNumber = ord(letters[i]) - ord('A')
            # Perform the decryption by subtracting the key value from the letter value (mod 27)
            DecryptedNumber = LetterNumber - KeyNumber
            if DecryptedNumber < 0:
                DecryptedNumber += 27
            # Convert the decrypted number back to a character
            if DecryptedNumber == 26:
                DecryptedCharacter = ' '
            else:
                DecryptedCharacter = chr(DecryptedNumber + ord('A'))
            DecryptedCharacters += DecryptedCharacter
            # Print the step-by-step process of decryption
            print(f"{Letter}({LetterNumber}) - {Key}({KeyNumber}) = {DecryptedCharacter}({DecryptedNumber})")
        print("-----------------")
        print(f"Decrypted letters: {DecryptedCharacters}")
        
        return DecryptedCharacters