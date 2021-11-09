def encode(user_input, key):
    output = ""
    for ch in user_input:
        encode1 = chr(ord(ch) + key)
        output = output + encode1
    return output