

# Example 1: Creating a function

# def function_name():
#     print("This is my first function block")


# Example 2: Calling a function
# def function_name(number):
#     print(f"This is my {number} function block")



# function_name()

# Example 3: Calling function multiple times
# function_name("first")
# function_name("second")
# function_name("third")
# function_name("fourth")



# Example 4: Passing Argument(data) to function
# def function_name(current_number):
#     print(f"This is my {current_number} function block")
# function_name("three")



# Example 5: Passing multiple argument in function 

# def greating(time, name,  day):
#     print(f"Good {time} {name}, I did not see you in class on {day}.")

# greating("Morning", "John", "Friday")
# greating("Afternoon", "Tope", "Saturday")
# greating("Sam", "Saturday", "Afternoon")


# Example 6: Passing argment as keyworld. This addresses the one of the problem with argument
# def greating(time, name,  day):
#     print(f"Good {time} {name}, I did not see you in class on {day}.")

# greating("Tope", "Saturday", "Afternoon")
# greating( name="Sam", day="Monday", time ="Morning")

# Example 7: Passing multiple  argument using  *args
# # *arg is a list of argument and you can access them using the same way you us access items in a list
# def greating(*args):
#     # Accressing infinite *arg
#     print(f"Good {args[0]} {args[1]}, I did not see you in class on {args[2]}.")

# # greating("Morning", "John", "Friday", "In Market")
# greating("Afternoon", "Tope", "Saturday")
# greating( args[0] ="Morning", args[1]="Sam", args[3]="Monday")

# Passing a default parameteer value
# Example 8: Passing keywork as argument

# def greating( time="day", name = "Chere" ,  day = "Wednesday"):
#     print(f"Good {time} {name}, I did not see you in class on {day}.")

# greating()
# # greating("Morning", "Sam", "Monday" )
# greating(name="Captain", day="Monday", time ="Morning")

# # Passing unlimited number of keyword as argument
# def greating( **kwargs):
#     print(f"Good {kwargs["time"]} {kwargs["name"]}, I did not see you in class on {kwargs["day"]}.")


# greating( )
# greating("Morning","Sam", "Monday" )
# greating(time = "Morning", name ="Sam", day ="Monday" )

# # Example 9:  Passing List as parameter

# fruits = ["Orange", "Banana", "Apple", "Grapes" ]

# def modify_fruits(fruits):
#     for each_fruit in fruits:
#         print(each_fruit)
#         print(each_fruit.upper())
#         print(f"The index of {each_fruit} is: {fruits.index(each_fruit)}")

# # modify_fruits(["Orange", "Banana", "Apple", "Grapes" ])
# modify_fruits(["water", "cocoa", "pepsi", "beer" ])




# Example 10: Returning a value
# To let a function return a value, use the return statement

def modify_fruits(fruits):
    uppercase_fruits_box = []
    for each_fruit in fruits:
       upper_fruit = each_fruit.upper()
       uppercase_fruits_box.append(upper_fruit)
    return uppercase_fruits_box


# A all words to be uppercase and make plural
def turn_value_to_plural(fruits):
    uppercase_fruit = modify_fruits(fruits)
    plural_box = []
    for item in uppercase_fruit:
        new_plural_fruit = item + "S"
        plural_box.append(new_plural_fruit)
    return plural_box
    

turn_value_to_plural(["Orange", "Banana", "Apple", "Grapes" ])