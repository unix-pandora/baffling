import casket


def encryption(plain, key):
    plain_text = str(plain).strip()
    key_text = str(key).strip()

    if key_text == None or plain_text == None:
        print("src/public/advance_cryptography.encryption: Error")
        return False

    key_word = casket.completion_string(key_text)
    cipher_context = casket.encrypt(key_word, plain_text)
    return cipher_context


def decryption(cipher, key):
    cipher_text = str(cipher).strip()
    key_text = str(key).strip()

    if key_text == None or cipher_text == None:
        print("src/public/advance_cryptography.decryption: Error")
        return False

    key_word = casket.completion_string(key_text)
    plain_context = casket.decrypt(key_word, cipher_text)
    return plain_context
