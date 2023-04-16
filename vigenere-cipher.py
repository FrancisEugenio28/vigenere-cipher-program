#Francis Niño A. Eugenio
#BSCPE 1-5 | Object Oriented Programing
#Program 3

import colorama
import pyfiglet

colorama.init()

# Create an input function for message and for the key
message = input(colorama.Fore.LIGHTMAGENTA_EX + "Please enter your Message: ")
key = input(colorama.Fore.LIGHTMAGENTA_EX + "Please enter your key: ")
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
        cipher_code = (message_code + key_code) % 26
# Gather the Cipher text with the ASCII code then return it to the empty set 
        cipher_code += 65
        cipher_text += chr(cipher_code)

    return cipher_text
# Add a loading effect
import time
print(colorama.Back.LIGHTYELLOW_EX + "Decoding...".center(150))
time.sleep(3)
# print the empty set or the output
cipher_text = vigenere_cipher(message,key)
print(pyfiglet.figlet_format(cipher_text, font = "bubble" ))