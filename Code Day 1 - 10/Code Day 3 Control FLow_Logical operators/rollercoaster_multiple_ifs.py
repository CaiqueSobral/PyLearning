print("Welcome to the Rollercoaster!")
height = int(input("What is yout height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Child tickets are R$5,00")
        bill = 5
    elif age <= 18:
        print("Youth tickets are R$7,00")
        bill = 7
    else:
        print("Adult tickets are R$12,00")
        bill = 12
    
    wants_photo = input("Do you want a photo? Y or N. ").upper()
    if wants_photo == "Y":
        bill += 3
        print(f"You have to pay R${bill}")
    else:
        print(f"You have to pay R${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")