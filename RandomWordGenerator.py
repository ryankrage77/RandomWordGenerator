#Ryankrage77's Random Word Generator
#Generates random pronouncable strings of a specified length.

import random

while True:
    stringLength = input("String length: ")
    while Genlength <= stringLength:
        #pick random letter
        #check  if letter is consonant or vowel
        #if vowel, go back through word by up to 3 places to check for vowels
        #reject letter if they are, add to list if not
        #if consonant, check if up to last 2 letters are consonants
        #reject if they are, add if not
        #repeat?
