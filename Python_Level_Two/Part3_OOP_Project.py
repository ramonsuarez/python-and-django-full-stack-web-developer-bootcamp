#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
# List comprehension do create deck of cards
# all_cards = [(r,s) for r in RANKS for s in SUITE]
class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.cards = [(r,s) for r in RANKS for s in SUITE]

    def shuffling(self):
        print('Shuffling')
        # Shuffle cards in place (will change original cards list of tuples)
        shuffle(self.cards)
    # Create decks for each player. p2 is computer
    def handling(self):
        print('Handing cards to players')
        self.dp1 = self.cards[:26]
        self.dp2 = self.cards[26:]

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    # I don't get it, copied from solution. How does this class know about the
    # cards in the deck?

    def __init__(self):
        self.cards = cards
    # Return length of the deck to see how many are left
    def __str__(self):
        return "Has {} cards".format(len(self.cards))

    def add_cards(self, won_cards):
        self.extend(won_cards)

    def remove_cards(self):
        self.pop(lost_cards)

class Player(Deck):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self):
        self.player = (input('Name of player?\t'))
    def __str__(self):
        return '{}'.format(self.player)
######################
#### GAME PLAY #######
######################
p1 = Player()
p2 = 'Computer'

print("Welcome {}. You are playing against {}\nLet's begin...WAR!".format(p1,p2))

d = Deck()
d.shuffling()
d.handling()

print(d.dp1)
# Use the 3 classes along with some logic to play a game of war!
