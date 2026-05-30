class PlayFairCipher:
    def __init__(self) -> None:
        pass
        
    def create_playfair_matrix(self, key: str):
        key = key.replace("J", "I").upper()
        seen = set()
        unique_key_chars = []
        for letter in key:
            if letter not in seen and letter.isalpha():
                seen.add(letter)
                unique_key_chars.append(letter)
                
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
        
        remaining_letters = [letter for letter in alphabet if letter not in seen]
    
        matrix_flat = unique_key_chars + remaining_letters
        playfair_matrix = [matrix_flat[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        plain_text = "".join([c for c in plain_text if c.isalpha()])
        prepared_text = ""
        i = 0
        while i < len(plain_text):
            prepared_text += plain_text[i]
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i+1]:
                    prepared_text += "X"  
                    i += 1
                else:
                    prepared_text += plain_text[i+1]
                    i += 2
            else:
                prepared_text += "X"  
                i += 1

        encrypted_text = ""
        for i in range(0, len(prepared_text), 2):
            pair = prepared_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:  
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2: 
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
        banro = ""
        i = 0
        while i < len(decrypted_text):
            if i + 2 < len(decrypted_text) and decrypted_text[i+1] == 'X' and decrypted_text[i] == decrypted_text[i+2]:
                banro += decrypted_text[i] + decrypted_text[i+2]
                i += 3
            else:
                banro += decrypted_text[i]
                i += 1
        if banro.endswith('X'):
            banro = banro[:-1]
            
        return banro