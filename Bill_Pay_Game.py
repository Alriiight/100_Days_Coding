# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_friends = len(names)
# print(num_friends)
# print(type(num_friends))
friend_minus1 = num_friends - 1
# print(friend_minus1)

friend_selector = random.randint(0, friend_minus1)
# print(friend_selector)

payer = names[friend_selector]
print(f"{payer} is going to buy the meal today!")