text = input("Input text:").lower()
def encrypt(text):
    encrypted = ""
    for i in range(len(text)):
        if text[i] == "z":
            encrypted += "b"
        elif text[i] == "y":
            encrypted += "a"
        elif text[i] == " ":
            continue
        elif not text[i].isalpha():
            encrypted += text[i]
        else:
            encrypted += chr(ord(text[i]) + 2)
    return encrypted

def decrypt(encrypted_text):
    decrypted = ""
    for i in range(len(encrypted_text)):
        if encrypted_text[i] == "b":
            decrypted += "z"
        elif encrypted_text[i] == "a":
            decrypted += "y"
        elif not encrypted_text[i].isalpha():
            decrypted += encrypted_text[i]
        else:
            decrypted += chr(ord(encrypted_text[i]) - 2)
    return decrypted

encryption = encrypt(text)
print(encryption)

decryption = decrypt(encryption)
print(decryption)

