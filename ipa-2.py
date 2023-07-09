#!/usr/bin/env python
# coding: utf-8

# In[39]:


# Shift a letter right by the given number.
# Wrap the letter around if it reaches the end of the alphabet.

letter = "" #letter shifted
shift = "_" #no of positions shifted to the right

def shift_letter(letter, shift):
    if letter == "" and shift == "_":
        return " "
    else:
        letter = letter.upper()
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index = (alphabet.index(letter) + shift) % 26 #keeps index within range
        shifted_letter = alphabet[index]
        return shifted_letter

shifted_letter = shift_letter(letter, shift)
print(shifted_letter)


# In[50]:


# Apply a shift number to a string of uppercase English letters and spaces.

message = "hello world"
shift = 2 #position shifted to the right per letter

def caesar_cipher(message, shift):
    shifted_message = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in message: #iterates over each letter in message
        if letter.isalpha():
            letter = letter.upper()
            index = (alphabet.index(letter) + shift) % 26
            shifted_letter = alphabet[index]
        else: #considers the spaces
            shifted_letter = letter
        
        shifted_message += shifted_letter #keeps the shifted letters in order
   
    return shifted_message

shifted_message = caesar_cipher(message, shift)
print(shifted_message)


# In[52]:


# Shift a letter to the right using the number equivalent of another letter.
# The shift letter is any letter from A to Z, where A represents 0, B represents 1, ..., Z represents 25.

letter = ""  # letters shifted
letter_shift = "_"  # no of positions shifted right 

def shift_by_letter(letter, letter_shift):
    if letter == "" and letter_shift == "_":
        return " "
    else:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        shift = alphabet.index(letter_shift.upper()) #letter represents number
        shifted_index = (alphabet.index(letter.upper()) + shift) % 26
        shifted_letter = alphabet[shifted_index]
    return shifted_letter

shifted_letter = shift_by_letter(letter, letter_shift)
print(shifted_letter)


# In[32]:


# Encrypts a message using a keyphrase instead of a static number.
# Every letter in the message is shifted by the number represented by the respective letter in the key.
# Spaces should be ignored.

message = "A C"
key = "key"

def vigenere_cipher(message, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_message = ""   
    message = message.upper()
   
    for letter in range(len(message)): #iterates over each letter
        key_letter = key[letter % len(key)] #keep string within range
        message_letter = message[letter]
        
        if key_letter != " " and message_letter != " ":
            shift = alphabet.index(key_letter.upper()) #letter represents number
            index = (alphabet.index(message_letter.upper()) + shift) % 26
            shifted_letter = alphabet[index]
            shifted_message += shifted_letter
        else:
            shifted_message += " "
    
    return shifted_message

shifted_message = vigenere_cipher(message, key)
print(f"vigenere_cipher: {message}, {key} ->", shifted_message)


# In[47]:


message = "INFORMATION_AGE"
shift = 3

def scytale_cipher(message, shift):
    encoded = ""
    message = message.upper()

    if len(message) % shift != 0: #check if length of the message is a multiple of shift
        additional = shift - (len(message) % shift)
        message += "_" * additional

    for i in range(len(message)):
        index = (i // shift) + (len(message) // shift) * (i % shift)
        encoded += message[index]

    return encoded

encoded = scytale_cipher(message, shift)
print(encoded)


# In[8]:


# Decrypts a message that was originally encrypted with the `scytale_cipher` function above.
message = "IMNNA_FTAOIGROE"
shift = 3

def scytale_decipher(message, shift):
    decoded = ""
    message = message.upper()
    zero = 0

    while zero < shift:
        for i in range(zero,len(message),shift):
            row = message[i]
            decoded += row
        zero += 1

    return decoded

decoded = scytale_decipher(message, shift)
print(decoded)

