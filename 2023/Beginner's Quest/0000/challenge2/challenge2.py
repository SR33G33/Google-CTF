# DOESNT WORK DID BY HAND

# MONO-ALPHABETIC SUBSTITUTION CIPHER SOLVER

from collections import Counter
from cipher_solver.simple import SimpleSolver
import string

# Typical frequency of letters in English
# ENGLISH_FREQ_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

# def frequency_analysis(ciphertext):
#     # Count the frequency of each letter in the ciphertext
#     counter = Counter(char for char in ciphertext.upper() if char in string.ascii_uppercase)
#     total = sum(counter.values())
    
#     # Sort the letters by frequency
#     freq_order = [char for char, _ in counter.most_common()]
#     return freq_order

# def create_decryption_key(initial_mapping, freq_order):
#     # Start with the known initial mapping
#     decryption_key = {char: initial_mapping[char] for char in initial_mapping}
    
#     # Add the remaining mappings based on frequency analysis
#     remaining_chars = [char for char in string.ascii_uppercase if char not in decryption_key]
#     remaining_freq_order = [char for char in freq_order if char not in decryption_key]
    
#     for i in range(len(remaining_chars)):
#         decryption_key[remaining_freq_order[i]] = remaining_chars[i]
    
#     return decryption_key

# def monoalphabetic_decrypt(ciphertext, decryption_key):
#     # Decrypt the ciphertext using the decryption key
#     plaintext = ''
#     for char in ciphertext:
#         if char.upper() in decryption_key:
#             if char.isupper():
#                 plaintext += decryption_key[char.upper()]
#             else:
#                 plaintext += decryption_key[char.upper()].lower()
#         else:
#             plaintext += char
#     return plaintext

# # Given text to decode
# ciphertext = "PDV KLRBC IOEXQ AEY TLGMF EJVO PDV NSWH ZEU. PDRF PVYP RF S MSQUOSG, XDRBD GVSQF PDSP RP BEQPSRQF SNN 26 NVPPVOF EA PDV VQUNRFD SNMDSIVP. PDRF GSCVF RP RZVSN AEO AOVKLVQBH SQSNHFRF, SF PDV BOHMPSQSNHFP BSQ BEGMSOV PDV AOVKLVQBH EA NVPPVOF RQ PDV BRMDVOPVYP PE PDV CQEXQ AOVKLVQBH EA NVPPVOF RQ PDV VQUNRFD NSQULSUV. AEO VYSGMNV, PDV GEFP BEGGEQ NVPPVO RQ PDV VQUNRFD NSQULSUV RF V. RA PDV GEFP BEGGEQ NVPPVO RQ PDV BRMDVOPVYP RF Y, PDVQ PDV BOHMPSQSNHFP BSQ SFFLGV PDSP Y RF NRCVNH PE IV S FLIFPRPLPREQ AEO V. EPDVO BEGGEQ NVPPVOF RQ PDV VQUNRFD NSQULSUV RQBNLZV P, S, E, R, Q, F, SQZ D. PDV BOHMPSQSNHFP BSQ LFV PDRF RQAEOGSPREQ PE GSCV VZLBSPVZ ULVFFVF SIELP PDV EPDVO FLIFPRPLPREQF RQ PDV BRMDVOPVYP. ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}"

# # Initial known mapping
# initial_mapping = {
#     'A': 'F',
#     'N': 'L',
#     'S': 'A',
#     'U': 'G'
# }

# # Perform frequency analysis on the ciphertext
# freq_order = frequency_analysis(ciphertext)

# # Create the decryption key based on initial mapping and frequency analysis
# decryption_key = create_decryption_key(initial_mapping, freq_order)

# # Decrypt the input text using the decryption key
# decrypted_text = monoalphabetic_decrypt(ciphertext, decryption_key)
# print("Decrypted Text: " + decrypted_text)
# print("Decryption Key: ", decryption_key)


# Solve a cipher.

with open("input.txt") as file:
    input_text = file.read().replace('\n', '')

s = SimpleSolver(input_text)
s.solve()
print(s.plaintext())  # "I am already far north of London."

# Solve using the original key swap method instead.
d = SimpleSolver(input_text)
d._solve_deterministic()
print(d.plaintext())