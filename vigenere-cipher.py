#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Program 3

# Create an input function for message and for the key
message = input("Please enter your Message: ")
key = input("Please enter your key: ")
# Repeat the length of the key base on the length of the Message
def vigenere_cipher(message,key):
    key_index = key * (len(message)// len(key) + 1)
    key_index = key_index[:len(message)]
# Create an empty set wherein we will put the output into it
    cipher_text = ''
# We will scan the characters in the message using a for loop 
    for i in range(len(message)):
        message_code = ord(message[i])
        key_code = ord(key_index[i])
# Gather the ASCII code both message and the key
        message_code -= 65
        key_code -= 65
# Perform the formulation of Vigenere Cipher Algorithm
# Gather the Cipher text with the ASCII code then return it to the empty set 
# print the empty set or the output