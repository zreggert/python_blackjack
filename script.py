import deck
# Player class 
class Player:
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll
    
    def __repr__(self):
        return (f"Ok {self.name}, you are starting out with ${self.bankroll}. Please place your first bet.")
    
    def place_bet(self):
        if self.bankroll == 0:
            self.buy_more_chips()
        else:
            print("How much would you like to bet?")
            while True:
                try:
                    self.bet = int(input())
                    if self.bet < 5:
                        print("The table minimum per hand is $5.\n")
                    elif self.bet > self.bankroll:
                        print("Sorry, you do not have enough to money for that bet.\n")
                        self.buy_more_chips()
                    else:
                        return self.bet
                except ValueError:
                    print("Please enter a numeric value of at least $5 to play your next hand.\n")

    
    def player_hit(self, hand , deck_id):
        # print(hand)
        new_hand = deck.draw_a_card(deck_id, hand["hand"])
        hand["hand"] = new_hand
        print(hand["hand"])
        hand["player_sum"] = deck.sum_of_hand(hand["hand"])
        if hand["player_sum"] > 21:
            hand["move"] = "end hand"
            print(f"Sorry you bust with a {hand["player_sum"]}.")
        else:
            print(f"You now have {hand["player_sum"]}")

    def hit_or_stay(self, data):
        data["move"] = ""
        move = input("Hit? or Stay?\n").lower()
        if move != "hit" and move != "stay":
            print("Please enter either hit or stay.")
            # move = input("Hit? or Stay?\n").lower()
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

    def split(self, hand):
        # if deck.check_for_pair(hand):
        while True:
            split = input(f"Would you like to split your {hand[0][0]}s? Yes or No?\n").lower()
            try:
                if split == "no":
                    return False
                elif split == "yes":
                        # deck.split_hand(hand)
                    return True
                else:
                    print("Please enter either yes or no.")
            except: 
                pass
    
    def player_wins(self, hand):
        self.bankroll += hand["bet"]
        print(f"You win! you now have ${self.bankroll}.")

    def player_loses(self, hand):
        self.bankroll -= hand["bet"]
        print(f"Sorry, the dealer wins. You now have ${self.bankroll}")

    def buy_more_chips(self):
        if self.bankroll == 0:
            answer = input("Would you like to buy more chips to keep playing?\n")
            if answer == "yes":
                self.bankroll = int(input("How much would you like to buy?\n"))
                print(f"Great! You now have ${self.bankroll}. Please place your next bet.")
                start(self)
            else:
                print("Thank you for playing Blackjack. Come play again soon.")
                
        

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
        print("Please be sure to enter numeric value of the money you want to play with.\n")
        

def start(player):
    deck_id = deck.new_deck()
    deal(player, deck_id)


def deal(player, deck_data):
    bet = player.place_bet()
    hands = deck.deal_hands(deck_data)
    print(f"You have {hands["player_hands"]}.")
    print(f"Dealer is showing {hands["showing"]}")

    for hand in hands["player_hands"]:
        if deck.check_for_pair(hand):
            if player.split(hand):
                hands["player_hands"] = deck.split_hand(hand, deck_data)
    data = deck.get_game_data(hands, deck_data, bet)

    if check_for_blackjack(player, data):
        play_again(player, deck_data)
    else:
        play_hand(player, data)


def check_for_blackjack(player, data):
    for hand in data["player_hands"]:
        if hand["has_blackjack"] == True and data["dealer_has_blackjack"] == False:
            print("BLACKJACK!")
            player.player_wins(hand)
            return True
        elif data["dealer_has_blackjack"] == True:
            print("Dealer has Blackjack.")
            player.player_loses(hand)
            return True
        elif hand["has_blackjack"] == True and data["dealer_has_blackjack"] == True:
            print("Blackjack! Unfortunately dealer also has Blackjack. Player pushes.")
            return True
        else:
            return False



def play_hand(player, data):
    # print(data)
    deck_id = data["deck_id"]
    for hand in data["player_hands"]:
        if len(data["player_hands"]) >= 2:
            print(f"Playing hand {hand["hand"]}.")
        print(f"Sum of the hand is {hand["player_sum"]}.")
        while hand["move"] != "end hand":
            player.hit_or_stay(hand)
            if hand['move'] == "hit":
                player.player_hit(hand, deck_id)
                if hand["player_sum"] > 21:
                    player.player_loses(hand)
                    play_again(player, deck_id)
            elif hand['move'] == "stay":
                break
    # print(data)
    dealers_turn(player, data)

    play_again(player, deck_id)
        
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
    
    end_hand(player, data)
    
def end_hand(player, data):
    for hand in data["player_hands"]:
        if hand["move"] == "stay":
            if data["dealer_sum"] >= 17 and data["dealer_sum"] <= 21:
                print(f"Dealer has a {data["dealer_sum"]}")
                result = deck.compare_hands(hand, data)
                if result == "win":
                    player.player_wins(hand)
                elif result == "lost":
                    player.player_loses(hand)
                elif result == 'draw':
                    print(f"Both you and the dealer have a {data["dealer_sum"]}. Player pushes.")
            elif data["dealer_sum"] > 21:
                print(f"Dealer busts with a {data["dealer_sum"]}")
                player.player_wins(hand)

    data["move"] = "end hand"


def play_again(player, deck_id):

    if deck.check_deck(deck_id):
        deal(player, deck_id)
    else:
        start(player)


player1 = Player(name, bankroll)
start(player1)



    




