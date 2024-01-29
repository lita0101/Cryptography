def generate_table(key_chars):
    table = [list('ABCDEFGHIKLMNOPQRSTUVWXYZ')]
    key_chars = list(key_chars.upper())

    for char in key_chars:
        if char in table[0]:
            table[0].remove(char)

    new_table = key_chars + table[0]
    new_table = [new_table[i:i + 5] for i in range(0, len(new_table), 5)]

    return new_table

def find_position(table, char):
    for i, row in enumerate(table):
        if char in row:
            return i, row.index(char)
    return -1, -1

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    # Padding if the text length is odd
    if len(text) % 2 != 0:
        text += 'X'
    # Splitting into pairs of characters
    text = [text[i:i + 2] for i in range(0, len(text), 2)]
    return text

def encrypt(plain_text, key_chars):
    table = generate_table(key_chars)
    plain_text = preprocess_text(plain_text)
    cipher_text = ''

    for pair in plain_text:
        char1, char2 = pair[0], pair[1]
        row1, col1 = find_position(table, char1)
        row2, col2 = find_position(table, char2)

        if row1 == row2:
            cipher_text += table[row1][(col1 + 1) % 5]
            cipher_text += table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += table[(row1 + 1) % 5][col1]
            cipher_text += table[(row2 + 1) % 5][col2]
        else:
            cipher_text += table[row1][col2]
            cipher_text += table[row2][col1]

    return cipher_text

def decrypt(cipher_text, key_chars):
    table = generate_table(key_chars)
    cipher_text = cipher_text.upper()
    plain_text = ''

    for i in range(0, len(cipher_text), 2):
        char1, char2 = cipher_text[i], cipher_text[i + 1]
        row1, col1 = find_position(table, char1)
        row2, col2 = find_position(table, char2)

        if row1 == row2:
            plain_text += table[row1][(col1 - 1) % 5]
            plain_text += table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain_text += table[(row1 - 1) % 5][col1]
            plain_text += table[(row2 - 1) % 5][col2]
        else:
            plain_text += table[row1][col2]
            plain_text += table[row2][col1]

    # Removing any trailing 'X' added for padding
    if plain_text[-1] == 'X':
        plain_text = plain_text[:-1]

    return plain_text

key = 'AYO'
plain_text = 'MAHASISWA UDINUS'
cipher_text = encrypt(plain_text, key)
print('Cipher Text:', cipher_text)

decrypted_text = decrypt(cipher_text, key)
print('Decrypted Text:', decrypted_text)
