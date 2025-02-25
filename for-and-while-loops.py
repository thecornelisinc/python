# FOR LOOPS
# Iterating over a list

# Example 1:

# Iterating over a list of fruits
# fruits = ["Orange", "Banana", "Apple", "Grapes" ]
# for fruit in fruits:
#     print(fruit)

# WHILE LOOPS
# Counting until a condition is met
# Example 1
# Count until you reach 20
# count = 0
# while count < 20:
#     print("Count is", count)
#     # count = count + 1
#     count += 1

# while count < 20:
#     print("Count is", count)
#     count = count + 1
#     # count += 1


# Searching for an Ip Address
# user_Ip_address = ""
# while user_Ip_address != "10.9.1.20":
#     if user_Ip_address == "":
#         print("The IP address is empty")
#         user_Ip_address = input('Enter the user IP Address ?')
#     else:
#         print("This is not the IP adress")
#         user_Ip_address = input('Enter the user IP Address ?')


# Working with break and continue

# CONTINUE
# Continue is another name for skip the current and continue on the next one
# Example:
# fruits = ["Orange", "Banana", "Apple", "Grapes" ]
# for each_fruit in fruits:
#   if each_fruit == "Banana":
#       continue
# #   print(each_fruit)
#   print(each_fruit.upper())



# BREAK
# Break is mean from the current iteration/item stopped the entire process and exit
# Example:
fruits = ["Orange", "Banana", "Apple", "Grapes" ]
for volume in fruits:
#   print(each_fruit)
  if volume == "unencrypted":
      break
  print(volume.upper())
