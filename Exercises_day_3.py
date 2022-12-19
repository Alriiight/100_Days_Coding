
# EXERCISE 1

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# EXERCISE 2 - Even/Odd number checker

# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# even_check = number % 2
# # print(even_check)

# if even_check == 0:
#     print("This is an even number.")
# else:
#     print ("This is an odd number.")

# EXERCISE 3 - IF/ELIF/ELSE STATEMENTS

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")