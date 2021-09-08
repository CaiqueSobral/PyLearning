from art import logo
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    cls()
    print(logo)
    calculatorOn = True
    firstNumber = float(input("What is the first number? "))
    operationSymbol = input("What is the operation? select '+', '-', '*' or '/': ")
    secondNumber = float(input("What is the second number? "))

    calculation_function = operations[operationSymbol]
    result = calculation_function(firstNumber, secondNumber)

    print(f"{firstNumber} {operationSymbol} {secondNumber} = {result}")

    while calculatorOn:
        if input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation \n") ==  'y':
            firstNumber = result
            operationSymbol = input("Pick another operation: ")
            secondNumber = float(input("What is the next number? "))
            calculation_function = operations[operationSymbol]
            result = calculation_function(result, secondNumber)

            print(f"{firstNumber} {operationSymbol} {secondNumber} = {result}")
        else:
            calculatorOn = False
            calculator()

calculator()