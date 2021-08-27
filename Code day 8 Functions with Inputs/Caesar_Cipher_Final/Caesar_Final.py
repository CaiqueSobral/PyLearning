alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
answer = "yes"
from art import logo
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def caesar(text, shift, direction):
    encodedText = ""
    for letter in text:
        if not letter in alphabet:
            encodedText += str(letter)
        else:
            if direction == "encode":
                if alphabet.index(letter) + shift > (len(alphabet) - 1):
                        encodedText += alphabet[alphabet.index(letter) - len(alphabet) + shift]
                else:
                    encodedText += alphabet[alphabet.index(letter) + shift]
            elif direction == "decode":
                if alphabet.index(letter) - shift < 0:
                    encodedText += alphabet[alphabet.index(letter) + len(alphabet) - shift]
                else:
                    encodedText += alphabet[alphabet.index(letter) - shift]  
    print(f"The {direction}d text is {encodedText}")

while answer == "yes": 
    cls()
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    answer = input("Do you want to keep with the program, type ""yes"" or ""no"" \n").lower()
cls()