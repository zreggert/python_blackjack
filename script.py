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
        hand = data["player_hand"]
        deck_id = data["deck_id"]
        new_hand = deck.draw_a_card(deck_id, hand)
        data["player_hand"] = new_hand
        print(data["player_hand"])
        data["player_sum"] = deck.sum_of_hand(data["player_hand"])
        if data["player_sum"] > 21:
            data["move"] = "end hand"
            print(f"Sorry you bust with a {data["player_sum"]}.")
        else:
            print(f"You now have {data["player_sum"]}")

    def hit_or_stay(self, data):
        move = input("Hit? or Stay?\n").lower()
        if move != "hit" and move != "stay":
            move = input("Hit? or Stay?\n")
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
    
    def player_wins(self, data):
        self.bankroll += data["bet"]
        print(f"You win! you now have ${self.bankroll}.")

    def player_loses(self, data):
        self.bankroll -= data["bet"]
        print(f"Sorry, the dealer wins. You now have ${self.bankroll}")
        



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
    deck_id = deck.new_deck()
    deal(player, deck_id)


def deal(player, deck_data):
    bet = player.place_bet()
    hand_data = deck.play_hand(bet, deck_data)

    if deck.check_for_blackjack(hand_data["player_sum"]) == True and deck.check_for_blackjack(hand_data["dealer_sum"]) == False:
        print("BLACKJACK! Dealer is checking their hand.")
        player.player_wins(hand_data)
    elif deck.check_for_blackjack(hand_data["dealer_sum"]) == True:
        print("Dealer has Blackjack.")
        player.player_loses(hand_data)
    elif deck.check_for_blackjack(hand_data["player_sum"]) == True and deck.check_for_blackjack(hand_data["dealer_sum"]) == True:
        print("Blackjack! Unfortunately dealer all so has Blackjack. Player pushes.")
    else:
        while hand_data["move"] != "end hand":
            player.hit_or_stay(hand_data)
            if hand_data['move'] == "hit":
                player.player_hit(hand_data)
                if hand_data["player_sum"] > 21:
                    player.player_loses(hand_data)
            elif hand_data['move'] == "stay":
                dealers_turn(player, hand_data)

    play_again(player, deck_data)

        
def dealers_turn(player, data):
    print("Dealers turn.")
    print(data["dealer_hand"])
    hand = data["dealer_hand"]
    deck_id = data["deck_id"]
    while data["dealer_sum"] < 17:
        new_hand = deck.draw_a_card(deck_id, hand)
        data["dealer_hand"] = new_hand
        print(new_hand)
        data["dealer_sum"] = deck.sum_of_hand(new_hand)
    
    if data["dealer_sum"] >= 17 and data["dealer_sum"] <= 21:
        print(f"Dealer has a {data["dealer_sum"]}")
        result = deck.compare_hands(data)
        if result == "win":
            player.player_wins(data)
        elif result == "lost":
            player.player_loses(data)
        elif result == 'draw':
            print(f"Both you and the dealer have a {data["dealer_sum"]}. Player pushes.")
    elif data["dealer_sum"] > 21:
        print(f"Dealer busts with a {data["dealer_sum"]}")
        player.player_wins(data)

    data["move"] = "end hand"

    # play_again(player, data)


def play_again(player, deck_data):
    if deck.check_deck(deck_data):
        deal(player, deck_data)
    else:
        start(player)







start(player1)







    




