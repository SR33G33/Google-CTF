def vigenere_decrypt(text, key):
    key_length = len(key)
    key_int = [ord(i.upper()) for i in key]
    decrypted = ''
    non_alpha_count = 0

    for i in range(len(text)):
        if text[i].isalpha():
            text_int = ord(text[i].upper()) - 65
            key_int_value = key_int[(i - non_alpha_count) % key_length] - 65
            decrypted_char = (text_int - key_int_value + 26) % 26 + 65
            
            if text[i].isupper():
                decrypted += chr(decrypted_char)
            else:
                decrypted += chr(decrypted_char).lower()
        else:
            decrypted += text[i]
            non_alpha_count += 1

    return decrypted



with open("input.txt") as file:
    input_text = file.read().replace('\n', '')

# Known key
key = "CAESAR"

# Decrypt the input text
decrypted_text = vigenere_decrypt(input_text, key)
print("Decrypted Text: " + decrypted_text)
print("Key: " + key)
