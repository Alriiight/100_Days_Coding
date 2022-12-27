# EXERCISE 3 - IF/ELIF/ELSE STATEMENTS

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

child_ticket = 5
youth_ticket = 7
adult_tickt = 12
photo_cost = 5

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Children tickets are $5.")
  elif age <= 18:
    print("Youth tickets are $7.")
  else:
    print("Adult tickets are $12.")

  input("Do you want a photo taken? Y or N. ")
  if input == "Y":
    print(f"Your total cost is {}")  
else:
  print("Sorry, you have to grow taller before you can ride.")