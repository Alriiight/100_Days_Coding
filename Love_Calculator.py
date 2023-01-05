# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Change to lower case.
name1.lower()
name2.lower()

# Count for true
num_t = name1.count("t") + name2.count("t")
# print(num_t)
num_r = name1.count("r") + name2.count("r")
# print(num_r)
num_u = name1.count("u") + name2.count("u")
# print(num_u)
num_e = name1.count("e") + name2.count("e")
# print(num_e)

num_true = num_t + num_r + num_u + num_e
print(f"Your 'true' score is {num_true}")