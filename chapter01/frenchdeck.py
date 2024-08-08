import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """
    Represents a deck of playing cards where
    each card has a rank and a suit.

    Attributes:
    _cards: A list of namedtuple Card where each Card has a rank from 2 to Ace and a suit (spades, diamonds, clubs, hearts).
    """

    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def get_random_card(self):
        return choice(self._cards)
