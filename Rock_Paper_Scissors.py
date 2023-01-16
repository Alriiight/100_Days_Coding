rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

if player_choice == "0":
    print(rock)
elif player_choice == "1":
    print(paper)
else:
    print(scissors)

computer_choice = str(random.randint(0, 2))
print(computer_choice)

if computer_choice == "0":
    print(rock)
elif computer_choice == "1":
    print(paper)
else:
    print(scissors)

if player_choice == "0" and computer_choice == "2":
    print("You win!")
else:
    print("You lose")

if player_choice == "1" and computer_choice == "0":
    print("You win!")
else:
    print("You lose")

if player_choice == "2" and computer_choice == "1":
    print("You win!")
else:
    print("You lose")