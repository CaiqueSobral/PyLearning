import random
import hangman_art
import hangman_words

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

endOfGame = False
chosenWord = random.choice(hangman_words.wordList)

display = []
lives = 6

for i in range(len(chosenWord)):
    display.append("_")

print(hangman_art.logo)
print(f'Pssst, the solution is {chosenWord}.')
print(f"{' '.join(display)}")


while not endOfGame:
    guess = input("Guess a letter: ").lower()

    cls()

    if guess in display:
      print(f"You've already guessed {guess}")

    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosenWord:
        lives -= 1
        print(f"You guessed {guess} that's not in the word, you lose a life")
        if lives == 0:
            endOfGame = True
            print("You lose")

    print(f"{' '.join(display)}")

    if not "_" in display:
        endOfGame = True
        print("You win")
    
    print(hangman_art.stages[lives])