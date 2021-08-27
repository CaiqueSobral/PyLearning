programmingDictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programmingDictionary["Function"])

programmingDictionary["Loop"] = "The action of doing something over and over again"
print(programmingDictionary)

#Create a new dictionary
emptyDictionary = {}

#Wipe out and dictionary
#programmingDictionary = {}

programmingDictionary["Bug"] = "A moth in your computer"

for thing in programmingDictionary:
    print(thing)
    print(programmingDictionary[thing])