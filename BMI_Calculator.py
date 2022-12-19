# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Step 1: confirm data type of variables.
# print(type(height))
# print(type(weight))

# Step 2: convert height ('str') into float.
fl_height = float(height)
# print(type(fl_height))

# Step 3: convert height ('str') into int.
num_weight = int(weight)
# print(type(num_weight))

# Step 4: Execute formula and create new BMI variable
BMI = (num_weight / (fl_height**2))

# Step 5: Convert result into int (float -> int). Print. 
BMI = int(BMI)
print(BMI)

# BMI Categories:
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

# Alternate method
# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)