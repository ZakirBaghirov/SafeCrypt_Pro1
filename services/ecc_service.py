from ecdsa import SECP256k1, SigningKey
import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import hashlib
import secrets

# Anahtar oluşturma ve kaydetme
def generate_keys():
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()
    return sk, vk

def save_keys(sk, vk, path='keys'):
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/private.pem", 'wb') as f:
        f.write(sk.to_pem())
    with open(f"{path}/public.pem", 'wb') as f:
        f.write(vk.to_pem())

def load_keys(path='keys'):
    with open(f"{path}/private.pem", 'rb') as f:
        sk = SigningKey.from_pem(f.read())
    with open(f"{path}/public.pem", 'rb') as f:
        vk = sk.get_verifying_key()
    return sk, vk

# AES şifreleme
def aes_encrypt(key: bytes, plaintext: str):
    iv = secrets.token_bytes(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return base64.b64encode(iv + ct).decode()

def aes_decrypt(key: bytes, ciphertext_b64: str):
    data = base64.b64decode(ciphertext_b64)
    iv = data[:16]
    ct = data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    pt = decryptor.update(ct) + decryptor.finalize()
    return pt.decode()

# ECC + AES şifreleme (ECIES)
def encrypt_with_ecc(message: str, vk):
    aes_key = secrets.token_bytes(32)  # 256-bit AES anahtarı
    encrypted_message = aes_encrypt(aes_key, message)
    signature = vk.to_string()
    derived_key = hashlib.sha256(signature).digest()
    encrypted_key = aes_encrypt(derived_key, base64.b64encode(aes_key).decode())
    return encrypted_key, encrypted_message

def decrypt_with_ecc(encrypted_key_b64: str, encrypted_message: str, vk):
    signature = vk.to_string()
    derived_key = hashlib.sha256(signature).digest()
    aes_key_b64 = aes_decrypt(derived_key, encrypted_key_b64)
    aes_key = base64.b64decode(aes_key_b64)
    decrypted_message = aes_decrypt(aes_key, encrypted_message)
    return decrypted_message
