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
        checkResource(drink["ingredients"])