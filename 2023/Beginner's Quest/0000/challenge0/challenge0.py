# Ceaser Cipher Decryption
def decrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)

        # Punctuation
        else:
            result += char

    return result
 
#check the above function
input = ""
s = 13
with open("input.txt") as file:
    for input in file:
        print ("Text  : " + input)
        print ("Shift : " + str(s))
        print ("Cipher: " + decrypt(input,s))