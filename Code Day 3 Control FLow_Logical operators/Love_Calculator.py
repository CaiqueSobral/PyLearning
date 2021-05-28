print("Welcome to the love calculator")
name1 = input("Type your name\n").lower()
name2 = input("Type their name\n").lower()

name12 = name1 + name2

love_score1 = name12.count("t") + name12.count("r") + name12.count("u") + name12.count("e")
love_score2 = name12.count("l") + name12.count("o") + name12.count("v") + name12.count("e")

love_score = int(str(love_score1) + str(love_score2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score},you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")