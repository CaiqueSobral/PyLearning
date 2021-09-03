def FormatName(firstName, lastName):
    if firstName == "" or lastName == "":
        return
    return (firstName + ' ' + lastName).title()

print(FormatName(input("What is your first name? "), input("What is your last name? ")))