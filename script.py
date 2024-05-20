# import requests

# Player class 
class Player:
    cards = []
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll
    
    def __repr__(self):
        return (f"Ok {self.name}, you are starting out with ${self.bankroll}. Please place your first bet.")
    
    def place_bet(self):
        print("How much would you like to bet?")
        while True:
            self.bet = int(input())
            if self.bet < 5:
                print("The table minimum per hand is $5.")
            elif self.bet > self.bankroll:
                print("Sorry, you do not have enough to money for that bet.")
            else:
                return self.bet


# At the start of the game the user will input the amount of money they wish to start the game with
name = input("Welcome to the blackjack table. What is your name?")
while True:
    try:
        name = int(name)
        print("Please enter a valid name.")
        name = input("Welcome to the blackjack table. What is your name?")
    except ValueError:
        break


while True:
    bankroll = input("How much money are you playing with today? The table minimum to play is $100 and the hand minimum is $5.\n")
    try:
        bankroll = int(bankroll)
        if bankroll >= 100:
            break
        else:
            print("You must start with at least $100.\n")
            continue
    except ValueError:
        print("Please be sure to enter numeric value of the money you want to play with.")
        

player = Player(name, bankroll)
bet = player.place_bet()



# Create a new deck of cards



# shuffle the deck of cards



    





