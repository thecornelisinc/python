# Working with List
# ============================


fruit1 = "Orange"
fruit2 = "Banana"
fruit3 = "Apple"
fruit4 = "Grape"


# # Using List as single variable
fruits = ["Orange", "Banana", "Apple", "Grape" ]   # index start zero 0
# # Accessing list Item using index positive and negative number
# print("best fruit: "+ fruit1)
# print("best fruit: "+ fruits[3])
# print("least favourite fruit: "+ fruits[-1])


# # Change item in  list
fruits[0] = "Strawberry"
# print(fruits)

# # Add to list item using append 
# Append add at the end
fruits.append("Coconut")
# print(fruits)

# # Add to list item using Insert
# # Insert to a specific index
fruits.insert(3, "Watermelon")
# print(fruits)


# # Remove from a list remove
fruits.remove("Apple")
# print(fruits)

# # Remove from a list using pop. This will remove item at index of number pass to pop
fruits.pop(1)
# print(fruits)

# # Loop over a list
# fruits = ["Orange", "Banana", "Apple", "Grapes" ]
# for each_fruit in fruits:
#   print(each_fruit)


fruits = ["Orange", "Banana", "Apple", "Grapes" ]
for each_fruit in fruits:
  print(each_fruit)
  print(each_fruit.upper())
  print(f"The index of {each_fruit} is: {fruits.index(each_fruit)}")

# Check the len of items in list
# To determine how many items a list has, use the len()
fruits = ["Orange", "Banana", "Apple", "Grapes" ]

print(len(fruits))

