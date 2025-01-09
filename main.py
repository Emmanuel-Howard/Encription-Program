# Encryption program that replaces passwords with random chars

# Import random + string modules
import random
import string

# Create chars with punctuation, digits, and letters
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)   # Turn chars into a list
key = chars.copy()    # Create a key (to shuffle the Encryption chars)

random.shuffle(key)   # Shuffle key so that the output is always different

# print(f"{chars}")   # Isn't needed in the program but useful to showcase
# print(f"{key}")     # the difference in Chars vs Key (Shuffled)

# ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
cypher_text = ""   # Empty string for coded message

for letter in plain_text:          # For each letter in the User's input
    index = chars.index(letter)    # Determine its position (index) in chars
    cypher_text += key[index]      # Add that position (in key) to cypher_text (coded message)

print(f"Encrypted Message: {cypher_text}")   # Prints coded message

# DECRYPTION
# Same process as encryption but switch cypher_text / plain_text
cypher_text = input("Enter a message to Decrypt: ")
plain_text = " "

for letter in cypher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted message: {cypher_text}")   # Prints coded message
print(f"Original message: {plain_text}")     # Prints original message