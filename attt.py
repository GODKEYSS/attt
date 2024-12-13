def permute_encrypt(plaintext, key):
    """
    Hàm mã hóa văn bản rõ bằng hoán vị.
    """
    if len(plaintext) != len(key):
        raise ValueError("Độ dài văn bản và khóa phải giống nhau.")
    
    plaintext = plaintext.upper()
    ciphertext = [''] * len(plaintext)
    for i in range(len(plaintext)):
        ciphertext[key[i] - 1] = plaintext[i]
    return ''.join(ciphertext)

def permute_decrypt(ciphertext, key):
    """
    Hàm giải mã văn bản mã hóa bằng hoán vị.
    """
    if len(ciphertext) != len(key):
        raise ValueError("Độ dài văn bản mã hóa và khóa phải giống nhau.")
    
    plaintext = [''] * len(ciphertext)
    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[key.index(i + 1)]
    return ''.join(plaintext)

def permute_encrypt_blocks(plaintext, key, m):
    """
    Hàm mã hóa văn bản theo từng nhóm m ký tự.
    """
    if len(key) != m:
        raise ValueError("Độ dài của khóa phải bằng số ký tự mỗi nhóm (m).")
    
    # Chia văn bản thành các nhóm m ký tự
    blocks = [plaintext[i:i + m] for i in range(0, len(plaintext), m)]
    
    ciphertext = ""
    for block in blocks:
        # Nếu nhóm cuối không đủ m ký tự, thêm ký tự đệm
        if len(block) < m:
            block += " " * (m - len(block))
        
        # Mã hóa từng nhóm
        ciphertext += permute_encrypt(block, key)
    
    return ciphertext.strip()

def permute_decrypt_blocks(ciphertext, key, m):
    """
    Hàm giải mã văn bản theo từng nhóm m ký tự.
    """
    if len(key) != m:
        raise ValueError("Độ dài của khóa phải bằng số ký tự mỗi nhóm (m).")
    
    # Chia văn bản thành các nhóm m ký tự
    blocks = [ciphertext[i:i + m] for i in range(0, len(ciphertext), m)]
    
    plaintext = ""
    for block in blocks:
        # Giải mã từng nhóm
        plaintext += permute_decrypt(block, key)
    
    return plaintext.strip()

# Ví dụ sử dụng
plaintext = "HENTOITHUBAY"
key = [3, 4, 1, 2, 6, 5]  # Khóa hoán vị, bắt đầu từ 1
m = 6  # Kích thước mỗi nhóm

# Mã hóa
ciphertext = permute_encrypt_blocks(plaintext, key, m)
print(f"Ciphertext: {ciphertext}")

# Giải mã
decrypted_text = permute_decrypt_blocks(ciphertext, key, m)
print(f"Decrypted text: {decrypted_text}")
