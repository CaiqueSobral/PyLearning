import random

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

userCards = []
computerCards = []

for i in range(2):
    userCards.append(dealCard())
    computerCards.append(dealCard())

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]