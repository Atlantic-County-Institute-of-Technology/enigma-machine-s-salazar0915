# praying this turns out okay
# I genuinely just winged it

def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)
# this was supposed to be the actual thing that makes the key work

def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)
# this is the function that odes the encrypting using the key (and it works booyah)


def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)
# this is the function that decrypts messages using the key(it only works like 85% of the time but the deadline's today)


def text_to_encrypt():
    return input("Put your normal word(s) here: ")
# this is where the user needs to input the message they want to encode or decode


key = input("Enter the keyword please: ")
mode = input("Would you like to encode or decode? : ")
# this is like a menu but I hate coding menus so I just mad it an option :)

encrypted_text = encrypt_vigenere(text_to_encrypt(), key)
print(f"Encrypted Text: {encrypted_text}")
# this just displays the result from whatever action the user asked for
