from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Buat key dan initialization vector
key = os.urandom(32)
iv = os.urandom(16)

# Buat cipher
backend = default_backend()
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)

# Buat padding dan unpadding object
padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

# Buat plaintext dan encrypt menjadi ciphertext
plaintext = b"Teknik Informatika"
padded_plaintext = padder.update(plaintext) + padder.finalize()
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

# Buat ciphertext dan decrypt menjadi plaintext
decryptor = cipher.decryptor()
padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()


binary_representation = ''.join(format(byte, '08b') for byte in ciphertext)
print()
print(f"Teks enkripsi: {binary_representation}")
print()
print(f"Teks deskripsi: {plaintext}")