def encrypt_message(message):
    import hashlib
    hash_func=hashlib.sha1()
    string_input=message
    encoded_string=string_input.encode()
    hash_func.update(encoded_string)
    encrypt_key=hash_func.hexdigest()
    return encrypt_key

