# Terminal Blackjack with Python

At the start of the game, user will be asked for input data that will be used to create a class instance of Player. Once the instance has been created the game will start and the user is asked to place a bet.

I've used the deckofcards api to create a 6 deck shoe of cards which the player will play with until less than 100 cards remain and a new 6-deck shoe will be generated with another API call.

The way I've decided to store the data for each hand is by using a python dictionary (object in javascript, but essentially variable with key:value pairs). The different class methods and deck functions essentially maniuplate the values until the end of the hand at which point they will update the player.bankroll variable depending on if the user wins or loses.