# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Change to lower case.
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

# Count for true
num_t = name1_lowercase.count("t") + name2_lowercase.count("t")
# print(num_t)
num_r = name1_lowercase.count("r") + name2_lowercase.count("r")
# print(num_r)
num_u = name1_lowercase.count("u") + name2_lowercase.count("u")
# print(num_u)
num_e = name1_lowercase.count("e") + name2_lowercase.count("e")
# print(num_e)

num_true = num_t + num_r + num_u + num_e
# print(f"Your 'true' score is {num_true}")

# Count for love
num_l = name1_lowercase.count("l") + name2_lowercase.count("l")
# print(num_l)
num_o = name1_lowercase.count("o") + name2_lowercase.count("o")
# print(num_o)
num_v = name1_lowercase.count("v") + name2_lowercase.count("v")
# print(num_v)
num_e = name1_lowercase.count("e") + name2_lowercase.count("e")
# print(num_e)

num_love = num_l + num_o + num_v + num_e
# print(f"Your 'love' score is {num_love}")

total_compatibility = str(num_true) + str(num_love)
print("Your love score is " + total_compatibility)

num_tot_comp = int(total_compatibility)

if num_tot_comp < 10 or num_tot_comp > 90:
    print(f"Your score is {num_tot_comp}, you go together like coke and mentos.")
elif num_tot_comp > 40 and num_tot_comp < 50:
    print(f"Your score {num_tot_comp}, you are alright together.")
else:
    print(f"Your score is {num_tot_comp}.")