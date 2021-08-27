alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encodedText = ""
    for letter in text:
        if alphabet.index(letter) + shift > (len(alphabet) - 1):
            encodedText += alphabet[alphabet.index(letter) - len(alphabet) + shift]
        else:
            encodedText += alphabet[alphabet.index(letter) + shift]   
    print(f"The encoded text is {encodedText}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)
