import random

rps = ['Rock', 'Paper', 'Scissors']

while True:
    user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors, 3 to Exit: "))
    
    if user_choice == 3:
        print("Exiting the game.")
        break
    computer_choice = random.randint(0, 2)
    if user_choice == computer_choice:
        print("!! IT'S A DRAW")
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        print(f"User Played {rps[user_choice]}")
        print(f"Computer Played {rps[computer_choice]}")
        print("Computer Wins")
    else:
        print(f"User Played {rps[user_choice]}")
        print(f"Computer Played {rps[computer_choice]}")
        print("User Wins")
