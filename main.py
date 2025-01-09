# Encryption program that replaces passwords with random chars

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"{chars}")
# print(f"{key}")

#Encrypt
plain_text = input("Enter a message to encrypt: ")
cypher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cypher_text += key[index]

print(f"Encrypted Message: {cypher_text}")

#DECRYPT
cypher_text = input("Enter a message to Decrypt: ")
plain_text = " "

for letter in cypher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cypher_text}")
print(f"Original message: {plain_text}")