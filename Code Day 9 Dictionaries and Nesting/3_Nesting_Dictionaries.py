#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary
travel_log = {
    "France": {
        "citiesVisited": ["Paris", "Dijon", "Lille"],
        "TotalVisits": 12 
    },
    "Germany":{
        "citiesVisited": ["Berlin", "Hamburgo", "Stuttgart"],
        "TotalVisits": 8
    }
}

#Nesting Dictionary in a List
travel_log = [
    {   
        "country":"France",
        "citiesVisited": ["Paris", "Dijon", "Lille"],
        "TotalVisits": 12 
    },
    {   
        "country":"Germany",
        "citiesVisited": ["Berlin", "Hamburgo", "Stuttgart"],
        "TotalVisits": 8
    }
]