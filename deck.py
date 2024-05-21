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
deck_id = new_deck()

# function to deal cards for a hand
def get_hand(deck_id):
    cards = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2')
    hand = []
    
    for item in cards.json()['cards']:
        card = (item['value'], item['suit'])
        hand.append(card)

    return hand



# play hand function will call get_hand function to create plaer and dealer hands
def play_hand():
    player_hand = get_hand(deck_id)
    player_sum = sum_of_hand(player_hand)

    dealer_hand = get_hand(deck_id)
    dealer_sum = sum_of_hand(dealer_hand)
    showing = dealer_hand[0]
    
    print(player_hand)
    print(f"You have a {player_sum}.")
    check_for_blackjack(player_sum)
    print(f"Dealer is showing {showing}.")

    if showing[0] == "ACE" or showing[0] == "KING" or showing[0] == "QUEEN" or showing[0] == "JACK":
        check_for_blackjack(dealer_sum)
    move = input("Hit? or Stay?")
    
    # need to make functionality for hitting or staying and adding the new values to the players hand 
    # also need validation to the users input 
    

# checks is a hand is a blackjack
def check_for_blackjack(num):
    if num == 21:
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
    return total



# play_hand()

