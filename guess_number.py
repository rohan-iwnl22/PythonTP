import random

print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 to 100")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

compGuess = random.randint(1, 100)
print(compGuess)

def play(lives):
    state = True
    while lives > 0 and state:
        print(f"You have {lives} left")
        try:
            userGuess = int(input("Enter your Guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number")
            continue
        if userGuess == compGuess:
            state = False
            print("You guessed it! You win!")
        elif compGuess-5 <= userGuess <= compGuess:
            print("You are almost there")
            lives -=1
        elif userGuess > compGuess:
            print("Too high\nGuess Again")
            lives -= 1
        elif userGuess < compGuess:
            print("Too low\nGuess Again")
            lives -= 1
    if lives == 0:
        print(f"You ran out of lives. The correct number was {compGuess}")


def get_difficulty(choice):
    if choice == "easy":
        return 10
    elif choice == "hard":
        return 5
    else:
        print("Invalid Choice. Exiting...")
        exit()


lives = get_difficulty(choice)
play(lives)


