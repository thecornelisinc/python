import json
import os 
import boto3

# Function Revision
# a. Static Function Defination

# def my_basic_function():
#     greetings = 'Good Morning, Yemi'
#     return greetings

# b. Calling Function
# my_basic_function()

# c. Dynamic function with string argument

# def my_basic_function(day, name):
#     greetings = f'Good {day}, {name}'
#     return greetings

# greeting_yemi = my_basic_function("Morning", "Yemi")
# greeting_tope = my_basic_function("Afternoon", "Tope")
# greeting_no_one = my_basic_function()
# print(greeting_no_one)
# print(greeting_yemi)

# # d. Dynamic function with key:value pair argument
# def my_basic_function(day = "Morning", name = "Sir"):
#     greetings = f'Good {day}, {name}'
#     return greetings


# print(my_basic_function())
# print(my_basic_function("Evening"))
# print(my_basic_function("Afternoon", "Tope"))

# # e. Passing list in a function

fruits = ["ORANGE", "APPLE", "BANANA", "APPLE"]


def peelFruit(fruits):
    boxForPeeledFruit = []
    for fruit in fruits: 
        peeledFruit = fruit.lower()
        boxForPeeledFruit.append(peeledFruit)
    return boxForPeeledFruit


print(peelFruit(fruits))


# # f. Passing object in a function

# import json

# def calculate_area(length, width):
#     return length * width


# context = {
#     "log_group_name": "area_log_data",
#     "env": "dev"
# }


# event = {
#     "length": 100,
#     "width": 50
# }
# def areaCalculator(event, context):
    
#     length = event['length'] 
#     width = event['width']
    
#     area = calculate_area(length, width)
#     print(f"The area is {area}")
        
#     # return the calculated area as a JSON string
#     data = {"area": area}
#     return json.dumps(data)


    

# areaCalculator(event, context)