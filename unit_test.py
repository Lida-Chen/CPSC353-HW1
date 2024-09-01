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
    pass

def test_CaesarDecrept():
    # TODO
    pass

def test_VigenèreEncrept():
    # TODO
    pass

def test_VigenèreDecrept():
    # TODO
    pass

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