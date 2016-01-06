import pokemon
import requests
from random import randint

class Player:
    """
    Create a player with a given name and set points to 0, and an empty deck
    """
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.deck = []
        self.won = None


    def create_deck(self, deck):
        """
        Assign the deck to the user
        """
        self.deck = deck

    def compare_first_card(self, other, stat):
        if(self.deck[0].compare(other.deck[0], stat)) == 0:
            return self
        else:
            return other

    def player_wins(self, opponent):
        winner_card = self.deck[0]
        loser_card = opponent.deck[0]
        del self.deck[0]
        self.deck.append(winner_card)
        self.deck.append(loser_card)
        return self

    def player_loses(self):
        loser_card = self.deck[0]
        del self.deck[0]
        return self