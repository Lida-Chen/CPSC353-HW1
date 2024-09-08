import unittest
import main_program
import CaesarCipher
import VigenèreCipher
import OneTimePad

def test_FormatCheck():
    assert main_program.FormatCheck("letters") == True
    assert main_program.FormatCheck("letters ") == True
    assert main_program.FormatCheck("letters123") == False

def test_CaesarEncrept():
    # TODO
    letters = "ABC D"
    encrypt_test = CaesarCipher.encrypt(letters)
    assert len(encrypt_test) == len(letters)
    for char in encrypt_test:
        assert(char.isupper() or char == ' ')

def test_CaesarDecrept():
    letters = "BCDAE"
    key = 'B'  # Example key for testing
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