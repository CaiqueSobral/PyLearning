travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def addNewCountry(country, visits, cities):
    newCountry = {}
    newCountry["country"] = country
    newCountry["visits"] = visits
    newCountry["cities"] = cities

    travel_log.append(newCountry)
    
#🚨 Do not change the code below
#addNewCountry("Russia", 2, ["Moscow", "Saint Petersburg"])
country = input("Qual país você visitou? \n")
visits = int(input("Quantas vezes você visitou o país? \n"))
cities = input("Quais cidades visitou? (Separe por virgula) \n").split(",")
addNewCountry(country, visits, cities)
print(travel_log)