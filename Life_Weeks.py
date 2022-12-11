# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days_left = (90 - int(age)) * 365
# print(days_left)

weeks_left = (90 - int(age)) * 52
# print(weeks_left)

months_left = (90 - int(age)) * 12
# print(months_left)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")