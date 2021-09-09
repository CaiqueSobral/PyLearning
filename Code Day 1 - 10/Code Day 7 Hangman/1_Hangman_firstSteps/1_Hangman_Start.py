import random
wordList = ["ardvark", "baboon", "camel"]

# ToDo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosenWord = random.choice(wordList)
print(chosenWord)

# ToDo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# ToDo-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
for letter in chosenWord:
    if letter == guess:
        print("Match")
    else:
        print("Wrong")