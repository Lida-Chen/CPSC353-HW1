import unittest
import main_program
import CaesarCipher
import VigenèreCipher
import OneTimePad

def test_FormatCheck():
    assert main_program.FormatCheck("letters") == True
    assert main_program.FormatCheck("letters ") == True
    assert main_program.FormatCheck("letters123") == False

def test_createkey_Caesar():
    key = CaesarCipher.CreateKey()
    assert(key >= 0 and key < 27)

def test_createkey_Vigenère():
    message = "ABC"
    keylen = 1
    key = VigenèreCipher.CreateKey(message,keylen)
    assert(len(key) == keylen*len(message))

def test_createkey_OneTime():
    message = "CAT"
    key = OneTimePad.CreateKey(len(message))
    assert(len(key) == len(message))


def test_CaesarEncrept():
    letters = "ABC D"
    encrypt_test = CaesarCipher.encrypt(letters)
    assert len(encrypt_test) == len(letters)
    for char in encrypt_test:
        assert(char.isupper() or char == ' ')

def test_CaesarDecrept():
    letters = "BCDAE"
    key = 'B'
    decrypted_text = CaesarCipher.decrypt(letters, key)
    assert len(decrypted_text) == len(letters)
    assert decrypted_text == "ABC D"

def test_VigenèreEncrept():
    letters = "HELLO WORLD"
    encrypted_text = VigenèreCipher.encrypt(letters, 4)
    assert len(encrypted_text) == len(letters)
    for char in encrypted_text:
        assert(char.isupper() or char == ' ')

def test_VigenèreDecrept():
    letters = "ABC"
    key = "ABC"
    decrypted_text = VigenèreCipher.decrypt(letters, key)
    assert len(decrypted_text) == len(letters)
    assert decrypted_text == "AAA"

def test_OneTimeEncrept():
    letters = "HELLO WORLD"
    encrypted_text = OneTimePad.encrypt(letters)
    assert len(encrypted_text) == len(letters)
    for char in encrypted_text:
        assert(char.isupper() or char == ' ')

def test_OneTimeDecrept():
    letters = "HELLO WORLD"
    key = OneTimePad.CreateKey(len(letters))
    decrypted_text = OneTimePad.decrypt(letters, key)
    assert len(decrypted_text) == len(letters)

if __name__ == '__main__':
    unittest.main()