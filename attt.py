def encrypt(text, key):
    """
    Mã hóa văn bản sử dụng hệ mật mã hoán vị.

    Args:
        text (str): Văn bản rõ cần mã hóa.
        key (list[int]): Khóa hoán vị.

    Returns:
        str: Văn bản đã mã hóa.
    """
    block_size = len(key)
    encrypted_text = []

    # Chia văn bản thành các khối độ dài bằng độ dài của khóa
    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]
        encrypted_text.append(permute_block(block, key))

    return ''.join(encrypted_text)

def decrypt(text, key):
    """
    Giải mã văn bản sử dụng hệ mật mã hoán vị.

    Args:
        text (str): Văn bản đã mã hóa.
        key (list[int]): Khóa hoán vị.

    Returns:
        str: Văn bản được giải mã.
    """
    block_size = len(key)
    reverse_key = [0] * block_size

    # Tạo khóa ngược
    for i, val in enumerate(key):
        reverse_key[val] = i

    decrypted_text = []

    # Giải mã các khối
    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]
        decrypted_text.append(permute_block(block, reverse_key))

    return ''.join(decrypted_text)

def permute_block(block, key):
    """
    Hoán vị các ký tự trong khối theo khóa.

    Args:
        block (str): Khối văn bản.
        key (list[int]): Khóa hoán vị.

    Returns:
        str: Khối sau khi hoán vị.
    """
    permuted = [''] * len(key)

    # Hoán vị các ký tự trong khối
    for i, char in enumerate(block):
        permuted[key[i]] = char

    return ''.join(permuted)

if __name__ == "__main__":
    plain_text = "HELLOWORLD"
    key = [3, 1, 4, 2, 0]  # Khóa hoán vị

    # Mã hóa
    encrypted_text = encrypt(plain_text, key)
    print("Văn bản mã hóa:", encrypted_text)

    # Giải mã
    decrypted_text = decrypt(encrypted_text, key)
    print("Văn bản giải mã:", decrypted_text)
