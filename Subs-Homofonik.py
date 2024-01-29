ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 'QWAESZRDXTFCYGVUHBIJNOKMPL'

key_pairs = {}

for i in range(len(KEY)):
    key_pairs[ALPHABET[i]] = KEY[i]
       
    
def encrypt(teks, key_pairs):
    teks = teks.upper()
    result = ""
    for i in teks:
        if i.isalpha():
            result += key_pairs.get(i)
        else:
            result += i
            
    return result

def decrypt(encrypted_teks, key_pairs):
    encrypted_teks = encrypted_teks.upper()
    result = ""
    for i in encrypted_teks:
        if i.isalpha():
            for alpha, key in key_pairs.items():
                if key == i:
                    result += alpha
                    break
        else:
            result += i
            
    return result

plaintext = "Aku memasak opor ayam"
encrypted = encrypt(plaintext, key_pairs)
decrypted = decrypt(encrypted, key_pairs)

print()
print(f"Teks yang terenkripsi: {encrypted}")
print()
print(f"Teks yang terenkripsi: {decrypted}")


