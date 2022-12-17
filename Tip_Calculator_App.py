# If the bill was $150.00, split between 5 people, with 12% tip. 

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# Step 1: Create all input requests and assign variable names to store data. 
print("Welcome to the tip calcular!\n")
bill_total = input("What was the total bill? ")
tip = input("What percentage would you like to tip? 10, 12, 15? ")
num_people = input("How many people are splitting the bill? ")

# Check data type of input variables.

# print(type(bill_total))
# print(type(tip))
# print(type(num_people))

# Step 2: Convert data type and figure out a way to create a new variable for percentage_tip that modifies multiplier value to be used with bill_total.

bill_total = float(bill_total)
tip = float(tip)
percentage_tip = (tip / 100) + 1
num_people = int(num_people)



# Check data type of new variables.

# print(type(bill_total))
# print(type(tip))
# print(type(tip))
# print(type(num_people))

# Add equation to calculate what each person must pay.

amount_per_person = (bill_total * percentage_tip) / num_people
amount_per_person = round(amount_per_person, 2)
amount_per_person = "{:.2f}".format(amount_per_person) # This gives format to the output, so that all floats are printed by 2 digits after the decimal point instead of 1 (ex. instead of showing $35.6 per person, it would print $35.60)
print(f"Each person should pay: ${amount_per_person}")