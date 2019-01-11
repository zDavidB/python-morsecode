# Python program to implement Morse Code Translator 
import re
from morse_class import MorseCoder

message = input("What is your message ?\n")

m = MorseCoder()

if re.search('^(\.|\-|\/)', message):
    print("Looks like an encrypted message, decrypting it")
    result = m.decrypt(message) 
else:
    print("Looks like a plain message, encrypting it")
    result = m.encrypt(message.upper())

print (result) 

