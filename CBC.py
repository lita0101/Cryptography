def cipher_block_chaining(key, message):
    size = 16

    # PKCS7 Padding
    padding_size = size - (len(message) % size)
    message += chr(padding_size) * padding_size

    # Encryption
    encrypted_text = ""
    for i in range(0, len(message), size):
        block = message[i:i + size]
        xor_block = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(block, key))
        encrypted_text += xor_block

    return encrypted_text

def cipher_block_chaining_decrypt(key, encrypted_text):
    size = 16

    decrypted_text = ""
    for i in range(0, len(encrypted_text), size):
        block = encrypted_text[i:i + size]
        xor_block = "".join(chr(ord(c) ^ ord(k)) for c, k in zip(block, key))
        decrypted_text += xor_block

    # Remove PKCS7 Padding
    padding_size = ord(decrypted_text[-1])
    decrypted_text = decrypted_text[:-padding_size]

    return decrypted_text



key = "ABCDEFGHIJKLMNOP"
message = "Halo Dinusian"

encrypted_text = cipher_block_chaining(key, message)
print("Text terenkripsi: ", encrypted_text)

decrypted_text = cipher_block_chaining_decrypt(key, encrypted_text)
print("Text terdekripsi: ", decrypted_text)