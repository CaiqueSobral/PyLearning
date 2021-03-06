import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def checkResource(orderIngredients):
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print("Sorry there is not enough {item}.")
            return False
    return True

def processCoins():
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transactionSuccess(moneyReceived, drinkCost):
    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False

def makeCoffe(drinkName, orderIngredients):
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here is your {drinkName} ☕")

profit = 0
machineOn = True

cls()
while machineOn:
    choice = input("What would you like? (espresso/latte/capuccino): ")

    if choice == "off":
        machineOn = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if checkResource(drink["ingredients"]):
            payment = processCoins()
            if transactionSuccess(payment, drink["cost"]):
                makeCoffe(choice, drink["ingredients"])