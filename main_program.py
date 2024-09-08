# Author: Lida Chen

import re
import argparse
import CaesarCipher
import VigenèreCipher
import OneTimePad

# check if the input string contains characters other than letters and space
def FormatCheck(letters : str):
    match = re.fullmatch(r"[A-Za-z\s]*", letters)
    if match is None:
        return False
    else:
        return True
    
# command line input format:
# python3 main_program.py encrypt Caesar letters --output
# python3 main_program.py decrypt Caesar letters --key e
def main():
    parser = argparse.ArgumentParser(description = "Encrypt or decrypt a string using a specified cipher.")
    parser.add_argument("option", type = str, choices = ["encrypt", "decrypt"], help = "Encrypt or decrypt")
    parser.add_argument("type", type = str, choices = ["Caesar", "Vigenere", "OneTimePad"], help = "Cipher type. Caesar, Vigenere, or OneTimePad")
    parser.add_argument("characters", type = str, help = "Characters need to be encrypted or decrypted")

    parser.add_argument("--key", type = str, help = "The key to use for decryption")# an optional argument for decrypting
    parser.add_argument("--output", action = "store_true", help = "Output ciphertexts to a file")
    parser.add_argument("--length", type = int, help = "The key to use for decryption")
    
    args = parser.parse_args()

    if FormatCheck(args.characters) is False:
        print("Please only enter letters and space")
        quit()
    else:
        args.characters = args.characters.upper()
        if args.option == "encrypt":
            ciphertext = ""
            if args.type == "Caesar":
                ciphertext = CaesarCipher.encrypt(args.characters)
            elif args.type == "Vigenere":
                if args.length is None:
                    print("A length is required for VigenèreCipher")
                    quit()
                print(args.length)
                ciphertext = VigenèreCipher.encrypt(args.characters, args.length)
            else:
                ciphertext = OneTimePad.encrypt(args.characters)
            if args.output:
                with open("ciphertext.txt", 'w') as file:
                    file.write(ciphertext)
                print("Ciphertext has been saved to ciphertext.txt")
        else:
            if args.key is None:
                print("A key is required for decryption")
                quit()
            else:
                if FormatCheck(args.key) is False:
                    print("Please only enter letters and space")
                    quit()
            args.key = args.key.upper()
            if args.type == "Caesar":
                CaesarCipher.decrypt(args.characters, args.key)
            elif args.type == "Vigenere":
                VigenèreCipher.decrypt(args.characters, args.key)
            else:
                OneTimePad.decrypt(args.characters, args.key)

if __name__ == "__main__":
    main()