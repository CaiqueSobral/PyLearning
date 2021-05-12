pizza_size = input("Which size of pizza do you want? S, M or L. ").upper()
add_pepperoni = input("Do you want to add pepperoni? Y or N. ").upper()
extra_chesse = input("Do you want extra chesse? Y or N. ").upper()
bill = 0

if pizza_size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_chesse == "Y":
        bill += 1
elif pizza_size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_chesse == "Y":
        bill += 1
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_chesse == "Y":
        bill += 1

print(f"Your final bill is R${bill}")

