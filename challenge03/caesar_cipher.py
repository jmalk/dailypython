# An implementation of the simple Caesar Cipher

class CaesarCipher(object):

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def encrpyt_plaintext(self, plaintext, shift_by):
        self.encrypt(plaintext, shift_by)

    def encrypt(self, text, shift):
        plaintext = text.upper()
        ciphertext = ""
        for character in plaintext:
            position_in_alphabet = self.alphabet.index(character)
            ciphertext += self.alphabet[position_in_alphabet + shift]
        print ciphertext



