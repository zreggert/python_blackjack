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

def check_deck(deck_id):
    response = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=0')
    # print(response.status_code)
    remaining = int(response.json()['remaining'])
    if remaining > 100:
        return True
    else:
        return False


# function to deal cards for a hand
def get_hand(deck_id):
    cards = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2')
    hand = []
    
    for item in cards.json()['cards']:
        card = (item['value'], item['suit'])
        hand.append(card)
    # test_hand_data = [('2', 'SPADES'), ('2', "HEARTS")]
    # return test_hand_data
    return hand

def draw_a_card(deck_id, hand):
    card_drawn = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1')

    for item in card_drawn.json()['cards']:
        card = (item['value'], item['suit'])
        hand.append(card)
    
    return hand

# function for splitting a list of cards into 2 lists of cards
def split_hand(hand, deck):
    print(hand)
    first_card = hand[:1]
    second_card = hand[1:]

    hand1 = draw_a_card(deck, first_card)
    hand2 = draw_a_card(deck, second_card)

    hands = [hand1,  hand2]
    print(hands)

    return hands

# play hand function will call get_hand function to create plaer and dealer hands
def deal_hands(deck):
    hands= {}

    player_hand = get_hand(deck)
    hands["player_hands"] = [player_hand]
    dealer_hand = get_hand(deck)
    hands["dealer_hand"] = dealer_hand
    hands["showing"] = hands["dealer_hand"][0]
    
    return hands


def get_game_data(hands, deck, bet):
    hand_data = {}
    hand_id = 1
    hand_data["deck_id"] = deck
    hand_data["dealer_hand"] = hands["dealer_hand"]
    hand_data["dealer_sum"] = sum_of_hand(hands["dealer_hand"])
    if hand_data["dealer_sum"] == 21:
        hand_data["dealer_has_blackjack"] = True
    else:
        hand_data["dealer_has_blackjack"] = False
        
    hand_data["player_hands"] = []
    for hand in hands["player_hands"]:
        new_hand = {}
        new_hand["hand_id"] = hand_id
        new_hand["hand"] = hand
        new_hand["player_sum"] = sum_of_hand(hand)
        if new_hand["player_sum"] == 21:
            new_hand["has_blackjack"] = True
        else:
            new_hand["has_blackjack"] = False
        new_hand["bet"] = bet
        new_hand["move"] = ""
        hand_data["player_hands"].append(new_hand)
        hand_id += 1

    return hand_data

# checks is a hand is a blackjack
# def check_for_blackjack(num):
#     if num == 21:
#         return True
#     else:
#         return False

# get the number value of a hand provided
def sum_of_hand(hand):
    total = 0
    for card in hand:
        if card[0] == "ACE":
            if total <=10:
                total += 11
            else:
                total += 1
        elif card[0] == "KING" or card[0] == "QUEEN" or card[0] == "JACK":
            total += 10
        else:
            total += int(card[0])
    
    return total

def compare_hands(hand, data):
    if hand["player_sum"] > data["dealer_sum"]:
        return "win"
    elif data["dealer_sum"] > hand["player_sum"]:
        return "lost"
    elif hand["player_sum"] == data["dealer_sum"]:
        return "draw"

def check_for_pair(hand):
    if hand[0][0] == hand[1][0]:
        return True


# test_hand = [('2', 'SPADES'), ('2', "HEARTS")]
# test_hand_data = {'player_hand': [('2', 'SPADES'), ('2', "HEARTS")]}



# check_for_pair(test_hand)


# new_deck()Portfolio Project: Terminal Game - Blackjack
# if check_for_pair(test_hand_data["player_hand"]):
#         split = input(f"Would you like to split your {test_hand_data["player_hand"][0][0]}s?")