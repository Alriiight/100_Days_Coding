import random

word_list = ["monkey", "ape", "car", "dog"]

print("Welcome to Hangman!")
print("Your goal is to guess the word before the character is hanged!")

ran_word = random.choice(word_list)
# print(ran_word)

letters_ran_word = list(ran_word)
# print(letters_ran_word)

user_guess = input("Type a letter: ").lower()
print(user_guess)

if user_guess 