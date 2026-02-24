class PlayfairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key: str):
        key = str(key)
        key = key.replace("J", "I").upper()
        key_set = []

        for ch in key:
            if ch not in key_set and ch.isalpha():
                key_set.append(ch)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # không có J
        for ch in alphabet:
            if ch not in key_set:
                key_set.append(ch)

        matrix = [key_set[i:i+5] for i in range(0, 25, 5)]
        return matrix

    def find_letter_coords(self, matrix, letter):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == letter:
                    return r, c

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        result = ""

        i = 0
        while i < len(plain_text):
            a = plain_text[i]
            b = plain_text[i+1] if i+1 < len(plain_text) else "X"

            if a == b:
                b = "X"
                i += 1
            else:
                i += 2

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == r2:
                result += matrix[r1][(c1 + 1) % 5]
                result += matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                result += matrix[(r1 + 1) % 5][c1]
                result += matrix[(r2 + 1) % 5][c2]
            else:
                result += matrix[r1][c2]
                result += matrix[r2][c1]

        return result

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        result = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i+1]

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == r2:
                result += matrix[r1][(c1 - 1) % 5]
                result += matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:
                result += matrix[(r1 - 1) % 5][c1]
                result += matrix[(r2 - 1) % 5][c2]
            else:
                result += matrix[r1][c2]
                result += matrix[r2][c1]

        return result
