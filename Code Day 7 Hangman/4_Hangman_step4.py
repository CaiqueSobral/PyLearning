import random
from typing import Deque
wordList = ["ardvark", "baboon", "camel"]

chosenWord = random.choice(wordList)
print(f'Pssst, the solution is {chosenWord}.')

display = []

for i in range(len(chosenWord)):
    display.append("_")
print(display)

endOfGame = False

while not endOfGame:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if not "_" in display:
        endOfGame = True

print("You win")