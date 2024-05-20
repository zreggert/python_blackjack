import requests

response = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6')
print(response.status_code)

print(response.json())
deck_id = response.json()['deck_id']
print(deck_id)

players_hand = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2')

total = 0
hand = []

for cards in players_hand.json()['cards']:
    
    card = (cards['value'], cards['suit'])
    hand.append(card)
    if cards['value'] == "ACE":
        total += 11
    elif cards['value'] == "KING" or cards['value'] == "QUEEN" or cards['value'] == "JACK":
        total += 10
    else:
        total += int(cards["value"])

print(f"You have {hand}")
print(total)

dealer_hand = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2')
# print(dealer_hand.json())
showing = dealer_hand.json()['cards'][0]["value"], dealer_hand.json()['cards'][0]["suit"]

print(f"Dealer is showing a {showing}")

