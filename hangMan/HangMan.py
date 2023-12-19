import random
from hanglogo import logo
import os

# importing logo from hanglogo file
print(logo)

# list of words for hangman
words = [
    "able",
    "about",
    "account",
    "acid",
    "across",
    "act",
    "addition",
    "adjustment",
    "advertisement",
    "after",
    "again",
    "against",
    "agreement",
    "air",
    "all",
    "almost",
    "among",
    "amount",
    "amusement",
    "and",
    "angle",
    "angry",
    "animal",
    "answer",
    "ant",
]

# chooses a random word
choosen_word = random.choice(words)

# sets the blank display list
display = []
# gives the lenght of randomly chose word
word_length = len(choosen_word)

# lives of user
stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

# number of life user has
lives = 6

# inputs the empty display list with " _ "
for _ in range(word_length):
    display.append("_")

# sets the base condition as false
end_of_game = False

# loop runs till condition is true which is when either user guesses all the word or runs out of lives
while not end_of_game:
    # takes input from the user
    guess = input("Guess A Letter:").lower()

    # clears the screen after every guess
    os.system('cls')

    # iterates through the word_length
    for position in range(word_length):
        letter = choosen_word[position] #letter is assigned the choosen_word ke postion index ka alphabet
        if letter == guess: #if user ka guess matches with the letter add the letter to display ka required index
            display[position] = letter

    if guess not in choosen_word: #if user ka guess doesnt matches with the letter print the corresponding stage ka index life
        # and decrement life by 1 and as soon as life is less then zero set the base condition true which in turn exits the game
        # showing you've lost the game
        print(stages[lives])
        lives -= 1
        if lives < 0:
            end_of_game = True
            print("You Lose")
    print(display)

    if "_" not in display: #if there are no empty spaces in the display list means user has guessed all of it correctly set the 
        # base condition true which exits the loop showing you've won the game
        end_of_game = True
        print("You win!")
