import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

wordList = ["ardvark", "baboon", "camel"]
endOfGame = False
chosenWord = random.choice(wordList)

display = []
lives = 6

for i in range(len(chosenWord)):
    display.append("_")
print(f"{' '.join(display)}")


while not endOfGame:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosenWord:
        lives -= 1
        if lives == 0:
            endOfGame = True
            print("You lose")

    print(f"{' '.join(display)}")

    if not "_" in display:
        endOfGame = True
        print("You win")
    
    print(stages[lives])