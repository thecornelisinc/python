# # 1. Basic Print Usage

# print("Hello world!")



# # 2. Printing Multiple Items

# name = "Sam"
# age = 30
# print("Name:", name, "\n", "Age:", age)



# 3.  Print in a file and not on terminal
with open("output.txt", "w") as file:
    print("This text goes into the file.", file=file)
