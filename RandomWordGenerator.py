#! /usr/bin/env python3
#Ryankrage77's Random Word Generator
#Generates random pronouncable strings of a specified length.

import random
word = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
currentLetter = ""
genLength = 0

while True:
    stringLength = input("String length: ")
    while genLength <= (int(stringLength) - 1):
        currentLetter = random.choice(alphabet)
        if currentLetter in vowels:
            if genLength >= 3:
                if word[(genLength - 1)] in vowels and word[(genLength - 2)] in vowels and word[(genLength - 3)] in vowels:
                    #print("Letter rejected, more than 3 vowels in a row")
                    pass
                else:
                    word.append(currentLetter)
                    genLength += 1
                    #print(word)
            else:
                word.append(currentLetter)
                genLength += 1
                #print(word)
        else:
            if genLength >= 2:
                if word[genLength - 1] not in vowels and word[genLength - 2] not in vowels:
                    #print("Letter rejected, more than 2 consonants in a row")
                    pass
                else:
                    word.append(currentLetter)
                    genLength += 1
                    #print(word)
            else:
                word.append(currentLetter)
                genLength += 1
                #print(word)

    word[0] = word[0].upper()
    fullWord = "".join(str(x) for x in word)
    print("Generated Word: ", fullWord)
    genLength = 0
    word = []
    continue
