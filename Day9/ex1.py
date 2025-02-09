travel_vlog = [
    {
        "country": "France",
        "visit" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visit" : 5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country_name, visited_city, name_of_cities = []):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = visited_city
    new_country["cities"] = name_of_cities
    travel_vlog.append(new_country)

add_new_country("Russia", 2, ["Moscow","Saint Petersbu"])
print(travel_vlog)
