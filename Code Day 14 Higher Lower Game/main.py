from art import logo, vs
from gameData import data
import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def formatData(account):
    accountName = account["name"]
    accountDescr = account["description"]
    accountCountry = account["country"]
    return (f"{accountName}, a {accountDescr}, from {accountCountry}")

def checkAnswer(guess, aFollowers, bFollowers):
    if aFollowers > bFollowers:
        return guess == "a"
    else:
        return guess == "b"

score = 0
keepGaming = True
accountB = random.choice(data)

while keepGaming:
    print(logo)
    accountA = accountB
    if accountA == accountB:
        accountB = random.choice(data)

    print(f"Compare A: {formatData(accountA)}")
    print(vs)
    print(f"Against B: {formatData(accountB)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    aFollowers = accountA["follower_count"]
    bFollowers = accountB["follower_count"]

    isCorrect = checkAnswer(guess, aFollowers, bFollowers)
    cls()
    print(logo)
    
    if isCorrect:
        score += 1
        print(f"You are right! Current Score: {score}")
    else:
        print(f"Sorry, you are wrong. Final score: {score}")
        keepGaming = False
