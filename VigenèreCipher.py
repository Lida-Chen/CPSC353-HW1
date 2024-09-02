# Author: Kyle Connall
# Date: 9/1/2024
# School: Gonzaga University
# Class: CPSC 353
# Description: Vigenere Cipher

import random
import string

letterDict = {"A":"0", "B":"1", "C":"2", "D":"3", "E":"4", "F":"5", "G":"6","H":"7", "I":"8", "J":"9","K":"10",
              "L":"11", "M":"12", "N":"13", "O":"14", "P":"15", "Q":"16", "R":"17", "S":"18", "T":"19", "U":"20",
              "V":"21", "W":"22", "X":"23", "Y":"24", "Z":"25", " ":"26"}
# create and print the key
def CreateKey(message,keylen = 4):
    letters = string.ascii_uppercase + ' '
    key = ''.join(random.choice(letters) for i in range(keylen))
    if len(message) > keylen:
        key = ''.join(key[i % keylen] for i in range(len(message)))
    elif len(message) < keylen:
        key = key[:len(message)]
    return key


# print the encrypted strings and how you get it
def encrypt(message, key):
    encrypted = []
    for i in range(len(message)):
        messageToNum = letterDict[message[i]]
        keyToNum = letterDict[key[i]]
        encryptedToNum = (str((int(messageToNum) + int(keyToNum)) % 27))
        encrypted.append(letterDict[str(encryptedToNum)])
    return ''.join(encrypted)

# print the decrypted strings and how you get it
# check if the key is legal
def decrypt(message, key):
    # TODO
    pass