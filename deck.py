import requests

# creating a shuffled deck. hard coding the deck count as 6. will modify later so the player can choose how many decks they want to play with.
def new_deck():
    response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6')
    # print(response.status_code)
    # print(response.json())
    # setting deck id to the id provided in the the api response
    deck = response.json()['deck_id']
    # print(deck_id)
    return deck

# deck id variable calls the new deck function to request api response with a new shuffled deck

# function to deal cards for a hand
def get_hand(deck_id):
    cards = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2')
    hand = []
    
    for item in cards.json()['cards']:
        card = (item['value'], item['suit'])
        hand.append(card)

    return hand

def draw_a_card(data):
    card_drawn = requests.get(f'https://deckofcardsapi.com/api/deck/{data['deck_id']}/draw/?count=1')

    for item in card_drawn.json()['cards']:
        card = (item['value'], item['suit'])
        data['player_hand'].append(card)
    
    return data


# play hand function will call get_hand function to create plaer and dealer hands
def play_hand(bet):
    hand_data = {}

    deck_id = new_deck()

    player_hand = get_hand(deck_id)
    player_sum = sum_of_hand(player_hand)

    dealer_hand = get_hand(deck_id)
    dealer_sum = sum_of_hand(dealer_hand)
    showing = dealer_hand[0]

    # putting data into a dictionary that will be returned at the end of the function. this data will be used to determine the class player method that will be envoked later
    hand_data["deck_id"] = deck_id
    hand_data["bet"] = bet
    hand_data["player_hand"] = player_hand
    hand_data["player_sum"] = player_sum
    hand_data["dealer_hand"] = dealer_hand
    hand_data["dealer_sum"] = dealer_sum
    
    print(player_hand)
    print(f"You have a {player_sum}.")
    check_for_blackjack(player_sum)
    # need to add functionality if player has blackjack
    print(f"Dealer is showing {showing}.")

    if showing[0] == "ACE" or showing[0] == "KING" or showing[0] == "QUEEN" or showing[0] == "JACK":
        check_for_blackjack(dealer_sum)
        # need to add fucntionality for if dealer has blackjack
    return hand_data
    

# checks is a hand is a blackjack
def check_for_blackjack(num):
    if num == 21:
        print("Blackjack!")
        return True
    else:
        pass

# get the number value of a hand provided
def sum_of_hand(hand):
    total = 0
    for card in hand:
        if card[0] == "ACE":
            total += 11
        elif card[0] == "KING" or card[0] == "QUEEN" or card[0] == "JACK":
            total += 10
        else:
            total += int(card[0])
    
    if total > 21:
        print("Bust, you lose.")

    return total

def compare_hands(data):
    if data["player_sum"] > data["dealer_sum"]:
        return "win"
    elif data["dealer_sum"] > data["player_sum"]:
        return "lost"



