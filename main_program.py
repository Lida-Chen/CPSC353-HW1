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
    # Add argument for encrypting or decrypting
    # Add the "option" argument to select between encryption and decryption
    parser.add_argument("option", type = str, choices = ["encrypt", "decrypt"], help = "Encrypt or decrypt")
    # Add argument for cipher type (Caesar, Vigenere, or OneTimePad)
    # Add the "type" argument to choose the cipher type (Caesar, Vigenere, or OneTimePad)
    parser.add_argument("type", type = str, choices = ["Caesar", "Vigenere", "OneTimePad"], help = "Cipher type. Caesar, Vigenere, or OneTimePad")
    # Add argument for the input string (characters to encrypt or decrypt)
    # Add the "characters" argument for the string that needs to be encrypted or decrypted
    parser.add_argument("characters", type = str, help = "Characters need to be encrypted or decrypted")
    # Optional argument for providing the decryption key
    # Optional argument for supplying the key during decryption
    parser.add_argument("--key", type = str, help = "The key to use for decryption")# an optional argument for decrypting
    # Optional argument to output ciphertext to a file
    # Optional argument to indicate whether to save the encrypted message to a file
    parser.add_argument("--output", action = "store_true", help = "Output ciphertexts to a file")
    # Optional argument for providing key length (used for Vigenère cipher encryption)
    # Optional argument to specify the key length for Vigenère cipher encryption
    parser.add_argument("--length", type = int, help = "The key to use for decryption")
    
    args = parser.parse_args()
    # Check if the input string contains only valid characters (letters and spaces)
    if FormatCheck(args.characters) is False:
        print("Please only enter letters and space")
        quit()
    else:
        args.characters = args.characters.upper()
        if args.option == "encrypt":
            ciphertext = ""
            # Handle Caesar cipher encryption
            if args.type == "Caesar":
                ciphertext = CaesarCipher.encrypt(args.characters)
            # Handle Vigenère cipher encryption
            elif args.type == "Vigenere":
                if args.length is None:
                    print("A length is required for VigenèreCipher")
                    quit()
                print(args.length)
                ciphertext = VigenèreCipher.encrypt(args.characters, args.length)
            # Handle One-Time Pad encryption
            else:
                ciphertext = OneTimePad.encrypt(args.characters)
            # Output the ciphertext to a file if specified
            if args.output:
                with open("ciphertext.txt", 'w') as file:
                    file.write(ciphertext)
                print("Ciphertext has been saved to ciphertext.txt")
        # If the operation is decryption
        else:
            # Ensure that a key is provided for decryption
            if args.key is None:
                print("A key is required for decryption")
                quit()
            # Check if the provided key is in a valid format
            else:
                if FormatCheck(args.key) is False:
                    print("Please only enter letters and space")
                    quit()
            args.key = args.key.upper()
            # Handle Caesar cipher decryption
            if args.type == "Caesar":
                CaesarCipher.decrypt(args.characters, args.key)
            # Handle Vigenère cipher decryption
            elif args.type == "Vigenere":
                VigenèreCipher.decrypt(args.characters, args.key)
            # Handle One-Time Pad decryption
            else:
                OneTimePad.decrypt(args.characters, args.key)

if __name__ == "__main__":
    main()