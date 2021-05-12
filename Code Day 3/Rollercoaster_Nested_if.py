print("Welcome to the Rollercoaster!")
height = int(input("What is yout height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay R$7,00")
    else:
        print("Please pay R$12,00")
else:
    print("Sorry, you have to grow taller before you can ride")