# Math in python


#f-string is an efficient way to convert data types within a single line of code in order to print to console. Use the following example for clarification:

# bmi = 27
# height = 1.80
# weight = 88
# is_overweight = True

# print(f"your height is {height} meters, your weight is {weight} kilograms. This means your BMI index is {bmi}. You are overweight is {is_overweight}.")

# LOGICAL OPERATORS
# and (both need to be true), or (one or the other must be true), not.

# ------------------------- DAY 4 -------------------------

# RANDOM MODULE

# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# random_combined = random_integer + random_float
# print(random_combined)

# LISTS

# states_of_america = ["Delaware", "Alabama", "Texas", "Pennsylvania"]
# print(states_of_america[1])
# # It is possible to have postive indecis and also negative ex. [-1].

# # Modify list element
# states_of_america[3] = "pencilvania"
# print(states_of_america)

# # Add element to list at the end. Use method append.
# states_of_america.append("Puerto Rico")
# print(states_of_america)

# # Add multiple elements to list. In esence, it combines lists and maintains the order, important to use square brackets, otherwise we become an error message for number of elements. Use method extend.
# states_of_america.extend(["El Salvador", "Iran", "Arabia Saudita"])
# print(states_of_america)

# ----------------------- NOTES DAY 5 ----------------------------
# For Loop

# FOR LOOP WITH RANGE
# Add from 1 - 100
 
# sum_result = 0
# for number in range(1,101):
#     sum_result += number

# print(sum_result)

for num in range(100):
    print(num) 

# ----------------------- NOTES DAY . ----------------------------
#  Took a break for a week due to covid. 