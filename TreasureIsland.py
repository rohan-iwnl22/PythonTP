print("Welcome to Treasure Island \n Your mission is to find the treasure.")
choice_1 = input("You've come across a division.There's a left and right. Which one you choose? LEFT OR RIGHT\n")
if choice_1 == 'RIGHT':
    print("Fall into a hole.Game Over.")
if choice_1 == 'LEFT':
    choice_2 = input("You've Come across a small river. What you wanna do? SWIM or WAIT\n")
    if choice_2 == 'SWIM':
        print("Attacked by trout.Game Over.")
    if choice_2 == 'WAIT':
        choice_3 = input("There are three doors infront of you, which one of them would you open?. RED BLUE YELLOW\n")
        if choice_3 == 'RED':
            print("Burned by fire.Game Over.")
        if choice_3 == 'BLUE':
            print("Eaten by beasts.Game Over.")
        if choice_3 == 'YELLOW':
            print("!! YOU WIN !!")
else:
    print("GAME OVER")
