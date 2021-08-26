import random
from typing import Deque
wordList = ["ardvark", "baboon", "camel"]

chosenWord = random.choice(wordList)
print(f'Pssst, the solution is {chosenWord}.')

display = []

for i in range(len(chosenWord)):
    display.append("_")
print(display)

# ADDED A WHILE LOOP
while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
    print(display)

print("You win")