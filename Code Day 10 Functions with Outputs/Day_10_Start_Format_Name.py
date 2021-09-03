
def FormatName(firstName, lastName):
    return (firstName + ' ' + lastName).title()

fName = input("What is your first name? ")
lName = input("What is your last name? ")

fullName = FormatName(fName, lName)

print(fullName)