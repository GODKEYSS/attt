# hệ mật mã hoán vị toàn cục python

import random


# hàm sinh khóa hoán vị
def generate_permutation_key(n):
    """Sinh khóa hoán vị ngẫu nhiên."""
    if n <= 0:
        raise ValueError("Độ dài thông điệp phải lớn hơn 0.")
    key = list(range(n))
    random.shuffle(key)
    return key

# hàm mã hóa
def encrypt(message, key):
    """Mã hóa thông điệp bằng khóa hoán vị."""
    if len(message) != len(key):
        raise ValueError("Độ dài thông điệp và khóa không khớp.")
    encrypted = ''.join(message[key[i]] for i in range(len(key)))
    return encrypted

# hàm giải mã
def decrypt(encrypted_message, key):
    """Giải mã thông điệp bằng khóa hoán vị ngược."""
    if len(encrypted_message) != len(key):
        raise ValueError("Độ dài bản mã và khóa không khớp.")
    n = len(key)
    inverse_key = [0] * n
    for i in range(n):
        inverse_key[key[i]] = i
    decrypted = ''.join(encrypted_message[inverse_key[i]] for i in range(n))
    return decrypted

message = "HELLO"
key = generate_permutation_key(len(message))
print("Khóa hoán vị:", key)

# Mã hóa
encrypted_message = encrypt(message, key)
print("Thông điệp mã hóa:", encrypted_message)

# Giải mã
decrypted_message = decrypt(encrypted_message, key)
print("Thông điệp giải mã:", decrypted_message)
