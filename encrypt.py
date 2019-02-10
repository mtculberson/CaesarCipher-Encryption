#!/usr/bin/python
import os

def main():
    MIN_ORDINAL_VALUE = 97
    MAX_ORDINAL_VALUE = 122
    
    key = int(input('Enter a key: '))
    inputFileName = input('Enter an input file name: ')
    outputFileName = input('Enter an output file name: ')

    f = open(inputFileName)
    file = f.read().lower()

    letters = list(file)

    outputFileText = ""
    for letter in letters:
        ordValue = ord(letter)
        if(ord(letter) <= MAX_ORDINAL_VALUE and ord(letter) >= MIN_ORDINAL_VALUE):
            ordValue += key
            
            if(ordValue > MAX_ORDINAL_VALUE):
                difference = ordValue - MAX_ORDINAL_VALUE
                ordValue = MIN_ORDINAL_VALUE + difference
            
        outputFileText += chr(ordValue)

    text_file = open(outputFileName, "w")
    text_file.write(outputFileText)
    text_file.close()

if __name__ == "__main__":
   main()




    
