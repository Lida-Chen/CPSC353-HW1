# Author: Kyle Connall
# Date: 9/1/2024
# School: Gonzaga University
# Class: CPSC 353
# Description: Vigenere Cipher

import random
import string
#Dictionary to convert letters to numbers
letterDict = {"A":"0", "B":"1", "C":"2", "D":"3", "E":"4", "F":"5", "G":"6","H":"7", "I":"8", "J":"9","K":"10",
              "L":"11", "M":"12", "N":"13", "O":"14", "P":"15", "Q":"16", "R":"17", "S":"18", "T":"19", "U":"20",
              "V":"21", "W":"22", "X":"23", "Y":"24", "Z":"25", " ":"26"}
#Dictionary to convert numbers to letters
numDict = {"0": "A", "1": "B", "2": "C", "3": "D", "4": "E", "5": "F", "6": "G", "7": "H", "8": "I", "9":"J",
           "10": "K", "11": "L", "12": "M","13": "N", "14": "O", "15": "P", "16": "Q", "17": "R", "18": "S",
            "19": "T", "20": "U", "21": "V", "22": "W", "23": "X", "24": "Y","25": "Z", "26": " "}
# create and print the key
def CreateKey(message,keylen = 4):
    letters = string.ascii_uppercase + ' '
    # Create the key to the length of 4
    key1 = ''.join(random.choice(letters) for i in range(keylen))
    # Match the key to the length of the message by using it over and over again.
    # If the key is shorter than the message, it will repeat.
    if len(message) > keylen:
        key = ''.join(key1[i % keylen] for i in range(len(message)))
    elif len(message) <= keylen:
        key = key1[:len(message)]
    print(key1)
    return key


# print the encrypted strings and how you get it
def encrypt(message, length):
    encrypted = []
    #Pass the key to the Dictionary to convert letters to numbers.
    #Pass the message to the dictionary to convert letters to numbers.
    #Add the numbers and mod 27 to get the encrypted message
    #Append the encrypted message to the list
    key1 = CreateKey(message)
    for i in range(len(message)):
        messageToNum = letterDict[message[i]]
        keyToNum = letterDict[key1[i]]
        encryptedToNum = (int(messageToNum) + int(keyToNum)) % 27
        #pass back into the reverse dictionary to get the letters back
        encrypted.append(numDict[str(encryptedToNum)])
    return ''.join(encrypted)

# print the decrypted strings and how you get it
# check if the key is legal
def decrypt(message, key):
    decrypted = []

    for i in range(len(message)):
        messageToNum = letterDict[message[i]]
        keyToNum = letterDict[key[i]]
        decryptedToNum = (int(messageToNum) - int(keyToNum)) % 27
        decrypted.append(numDict[str(decryptedToNum)])
    print(decrypted)
    return ''.join(decrypted)