#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Step 1: Create all input requests and assign variable names to store data. 
print("Welcome to the tip calcular!\n")
bill_total = input("What was the total bill? ")
percentage_tip = input("What percentage would you like to tip? 10, 12, 15? ")
num_people = input("How many people are splitting the bill? ")

# Check data type of input variables.

print(type(bill_total))
print(type(percentage_tip))
print(type(num_people))

# Step 2: Convert data type and figure out a way to create a new variable for percentage_tip that modifies multiplier value to be used with bill_total.

bill_total = float(bill_total)
percentage_tip = float(percentage_tip)
num_people = int(num_people)

# Check data type of new variables.

print(type(bill_total))
print(type(percentage_tip))
print(type(num_people))