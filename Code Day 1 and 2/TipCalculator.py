billValue = float(input("Full Bill value: "))
tipPercentage = int(input("Type the tip percentage you want to pay (Use only numbers): "))
peopleNumber = int(input("How many will split the bill: "))

finalBill = "{:.2f}".format(float(billValue + (billValue / 100 * tipPercentage)))
finalValue = "{:.2f}".format(float(finalBill) / peopleNumber)

print(f"The total amount is R${finalBill} and it will be splited as R${finalValue} for each one")
