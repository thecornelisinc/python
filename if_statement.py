x = 10
y = 10


# If Statement with One condition
# ====================================
# Example 1 with if only:
# if y > x:
#     print(f"y is greater than x")

# Example 2 with else:
# if y > x:
#     print(f"y is greater than x")
# else:
#     print(f"y is less than x")
    


# Example 3 with elif:
# if y > x:
#  print(f"y is greater than x")

# elif y < x:
#     print(f"y is less than x")
    
# else:
#  print(f"y is equal to x")

# Example 4: 
# state = "running"

# if state == "stopped":
#     print("Start the instance")

# elif state == "running":
#     print("Stop the instance")

# else: 
#     print("Instance is currently stopping or pending, wait for some minutes")


# If Statement with two condition
# ====================================

# is_Instance_Present = True
# region = "us-east-1"
# state = "running"

# if region != "us-east-1" and is_Instance_Present == True and state == "running":
#     print("Instance is NOT COMPLIANT")
#     print("Inform instance owner to migrate instance to us-east-1")
#     print("Stopped Instance after 3 days of Notifying instance owner")
#     print("Terminate instance afer 7 days of notifying owner")

# else: 
#     print("Instance is COMPLIANT")


# If Statement with not content
# You may decide not to put any instruction or information after the if statement

# Example
# state = "stopped"
# if state == "running":
#     pass
# else:
#     print("start the instance")