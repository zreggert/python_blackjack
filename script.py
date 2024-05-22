import deck
# Player class 
class Player:
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
    
    def player_hit(self, data):
        deck.draw_a_card(data)
        print(data["player_hand"])
        data["player_sum"] = deck.sum_of_hand(data["player_hand"])
        print(f"You now have {data["player_sum"]}")

    def hit_or_stay(self, data):
        while True:
            move = input("Hit? or Stay?\n").lower()
            if move != "hit" and move != "stay":
                move = input("Hit? or Stay?")
            elif move == "hit":
                # call hit function
                print("player hit")
                # draw_a_card(deck_id, player_hand)
                data["move"] = move
                return data
            elif move == "stay":
                #call stay function here
                print(f"player is staying on {data['player_sum']}")
                data["move"] = move
                return data
            else:
                print("something else")
        



# At the start of the game the user will input the amount of money they wish to start the game with
name = input("Welcome to the blackjack table. What is your name?\n")
while True:
    try:
        name = int(name)
        print("Please enter a valid name.")
        name = input("Welcome to the blackjack table. What is your name?\n")
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
        

player1 = Player(name, bankroll)

def start(player):
    bet = player.place_bet()
    hand_data = deck.play_hand(bet)

    while True:
        player1.hit_or_stay(hand_data)
        if hand_data['move'] == "hit":
            player1.player_hit(hand_data)
        elif hand_data['move'] == "stay":
            print("This is where we compare hands")
            print(hand_data)
        # This will be where we compare the player and dealer hands. also revealing the dealers hand to the player






start(player1)







    




