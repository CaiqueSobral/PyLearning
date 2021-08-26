def calculator(height, width, coverage):
    numberOfCans = round((height * width) / coverage)
    print(f"You will need to use {numberOfCans} cans of paint.")

calculator(3, 9, 5)