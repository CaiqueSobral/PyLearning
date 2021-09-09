import os
from art import logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def FindWinner(biddingRecord):
    highestBid = 0
    winner = ""

    for bidder in biddingRecord:
        bidAmount = biddingRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} with a bid of R${highestBid}")

bids = {}
finish = False

print(logo)


while not finish:
    name = input("What is your name? ")
    price = int(input("What is your bid? R$"))
    bids[name] = price

    keepGoing = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if keepGoing == "no":
        finish = True
    elif keepGoing == "yes":
        cls()

FindWinner(bids)