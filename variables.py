# Creating new variables

"""

How to create a variable:
        You don't create a variable. The moment you assign a value to another value on the left, a variable is created.
        See Example  below
"""


firstName = "Sam"
lastName = "Davis"

x = 20
y = "20"





# Variable Name Examples
# Good naming
# fullname = "Sam Devies"
# lastname_firstname = "Sam Devies"
# _lastname_firstname = "Sam Devies"
# lastName = "Davies"
# LASTNAME = "Davies"
# lastName2 = "Davies"


# Bad Naming
# 2fullname
# lastname-firstname
# lastname firstname 
# lastname.firstname 



# 1. Global Variable
# ======================

# x = "outside x"


# def myfunc():
#   print(x)

# myfunc()



# 2. local Variable
# ==========================
x = "ouside x"

def myfunc():
  x = "inside x"
  print(x)

myfunc()



# 3. local Variable limitation
# ==========================
x = "ouside x"

# def myfunc():
#   x = "inside x"
#   print("x in line 69: "+  x)

# myfunc()


# print("x in line 74: "+ x)



# 3. how to use local variable as global
# =====================================

def myfunc():
  global x
  x = "inside x"
  print("x in line 84: "+  x)

myfunc()

print("x in line 89: "+ x)















# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function