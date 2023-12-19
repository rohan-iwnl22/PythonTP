from art import logo
import os

cont = False

def winner(bidding):
    highest_amount = 0
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            champ = bidder
    print(f"Winner is {champ} with a bid of ${highest_amount}")


while not cont:
    print(logo)
    bidding = {}
    name = input("What is your name? ")
    price = int(input("Whats the amount you wanna bid for? $"))
    bidding[name] = price
    again = input("Are there any more players bidding? YES or NO.\n").lower()
    if again == "no":
        cont = True
        winner(bidding)
    elif again == "yes":
        os.system('cls')
    else :
        cont = True


