# Working with Dictionary
# Dictionaries are used to store data values in key:value pairs.

# Sample dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,

}


# Accessing Items in Dictionary
# brand = car["brand"]
# model = car["model"]
# year = car["year"]
# print(year)


# Adding item to Dictionary

# car["color"] = "red"
# car["year"] = 2025
# print(car)


# Remove item from dictiorary

# print(car)
# car.pop("color")
# print(car)

# Loop through Dictionary

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# # for info in car:
#   print(info)
#   print(car[info]) 
#   print(f"{info}: {car[info]}")


# Working with nested dictionary
cars = {
    "car1": {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    },
    "car2": {
        "brand": "Chevrolet",
        "model": "Corvette",
        "year": 2020
    },
    "car3": {
        "brand": "Toyota",
        "model": "Camry",
        "year": 2018
    },
    "car4": {
        "brand": "Honda",
        "model": "Civic",
        "year": 2020
    },
    "car5": {
        "brand": "BMW",
        "model": "M3",
        "year": 2021,
        "seller": { "Name": "John", "Location": "Kansas"}
    }
}

# using "get"Dictionary Methods to get item in dictionary
# print(cars.get("car3"))

# print(cars["car1"]["brand"])
print(cars["car5"]["seller"]["Location"])