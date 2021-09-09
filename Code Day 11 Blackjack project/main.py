from art import logo
import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore, computerScore):
    if userScore == computerScore:
        return "It's a Draw"
    elif computerScore == 0:
        return "Lose, opponent has a blackjack"
    elif userScore == 0:
        return "YOU WIN, YOU HAVE A BLACKJACK"
    elif userScore > 21:
        return "You went over. You lose"
    elif computerScore > 21:
        return "Opponent went over. You Win"
    elif userScore > computerScore:
        return "You win!!!"
    else:
        return "You lose"

def blackJack():
    print(logo)
    userCards = []
    computerCards = []
    gameOver = False

    for i in range(2):
        userCards.append(dealCard())
        computerCards.append(dealCard())


    while not gameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        print(f"    Your cards: {userCards}, current score: {userScore}")
        print(f"    computer's first card: {computerCards[0]}")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            gameOver = True
        else:
            getNewCard = input("Type 'y' to get another card, type 'n' to pass: ")
            if getNewCard == "y":
                userCards.append(dealCard())
            else:
                gameOver = True

    while computerScore	!= 0 and computerScore < 17:
        computerCards.append(dealCard())
        computerScore = calculateScore(computerCards)

    print(f"    Your final hand: {userCards}, final score: {userScore}")
    print(f"    Computer's hand: {computerScore}, final score: {computerScore}")
    print(compare(userScore, computerScore))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == "y":
    cls()
    blackJack()