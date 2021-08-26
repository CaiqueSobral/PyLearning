import random
wordList = ["ardvark", "baboon", "camel"]

chosenWord = random.choice(wordList)
print(chosenWord)

guess = input("Guess a letter: ").lower()

for letter in chosenWord:
    if letter == guess:
        print("Match")
    else:
        print("Wrong")