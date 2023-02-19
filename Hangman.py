
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list) # This variable stores the random word selected from the list above by the program. 
word_length = len(chosen_word) # Since I was using the len() multiple times, I created this variable for better readability and less typing.0

lives = 6 #Number of total lives (user guesses). If the guessed letter is not in the word, the lives will reduce by 1. If lives goes down to 0 the the game should stop and it should print "You lose.".

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = [] # I create this empty list in order to store the "spaces" for each letter and its position. It is used to show the user the empty spaces as underscores intead of the actual letters.

#Create blanks
for _ in range(word_length): 
  display += "_"
print(display)

# This for loop substitutes each letter from the chosen_word with an underscore. It works by adding one underscore per letter to the empty display list created before. Once it has looped through all the characters, it displays the list as ["_", "_", "_"]

end_of_game = False #Variable is created to properly execute a while loop to keep asking the user for input as long as there are empty spaces left. The Boolean will later change, so that once all empty spaces are filled with the corresponding letter, the value will be True and the while loop will end. 

while end_of_game == False: 
    guess = input("Guess a letter: ").lower()
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position] #This is used to individually select each letter of the chosen_word and store it in the letter variable to compare with the guessed letter from the user as follows.
        if letter == guess:
            display[position] = letter #Since the user's guess was actually equal to a letter in the chosen word, than the letter is added to the display list in the same position as compared in the previous loop step.
        else:
            lives -= 1
    print(display)

#Check if user has got all letters.
if "_" not in display:
    end_of_game == True

print(display)