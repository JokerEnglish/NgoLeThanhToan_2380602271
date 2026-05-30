class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = []
        key_index = 0
        key = key.upper() 
        
        for char in plain_text:
            if char.isalpha():
                key_char = key[key_index % len(key)]
                key_shift = ord(key_char) - ord('A')
                
                if char.isupper():
                    cipher_char = chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                    encrypted_text.append(cipher_char)
                else:
                    cipher_char = chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                    encrypted_text.append(cipher_char)
                
                key_index += 1
            else:
                encrypted_text.append(char)
   
        return "".join(encrypted_text)

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = []
        key_index = 0
        key = key.upper()
        
        for char in encrypted_text:
            if char.isalpha():
                key_char = key[key_index % len(key)]
                key_shift = ord(key_char) - ord('A')
                
                if char.isupper():
                    plain_char = chr((ord(char) - ord('A') - key_shift + 26) % 26 + ord('A'))
                    decrypted_text.append(plain_char)
                else:
                    plain_char = chr((ord(char) - ord('a') - key_shift + 26) % 26 + ord('a'))
                    decrypted_text.append(plain_char)
                
                key_index += 1
            else:
                decrypted_text.append(char)
                
        return "".join(decrypted_text)