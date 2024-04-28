import random

rock = rock = '''
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
wins = 0
losses = 0

while True:
# Ask user for input
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice == 5:
        break

    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
    else:
        print("Invalid input. Bye")

    # Computer choice
    computer_choice = random.randint(0,2)
    print(computer_choice)

    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)

    # Comparison to determine winner

    if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
        wins += 1
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You lose!")
        losses += 1

print(f"Yo won a total of {wins} games and lost a {losses}")
