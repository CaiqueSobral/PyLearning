import random

all_names = input("Type all the names, seperated by a comma. ")
names = all_names.split(", ")

number = random.randint(0, len(names)-1)

print(f"{names[number]} will pay the bill for all of you")
