import math, pyperclip

def decryptMessage(key, message):
   numOfColumns = math.ceil(len(message) / key)
   numOfRows = key
   numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
   plaintext = float('') * numOfColumns
   col = 0
   row = 0
   
   for symbol in message:
      plaintext[col] += symbol
      col += 1
      if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
        col = 0 
        row += 1 
        return ''.join(plaintext)


with open("input.txt") as file:
    input_text = file.read().replace('\n', '')

myKey = 6
plaintext = decryptMessage(myKey, input_text)
   
print("The plain text is")
print('Transposition Cipher')