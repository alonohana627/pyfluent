from chapter01.frenchdeck import *
import unittest


class FrenchDeckTest(unittest.TestCase):
    def test_len(self):
        deck = FrenchDeck()
        self.assertEqual(len(deck), 52)

    def test_contains(self):
        deck = FrenchDeck()
        self.assertIn(Card("A", "spades"), deck)
        self.assertIn(Card("2", "spades"), deck)
        self.assertIn(Card("3", "hearts"), deck)
        self.assertIn(Card("4", "clubs"), deck)
        self.assertIn(Card("5", "diamonds"), deck)

    def test_not_contains(self):
        deck = FrenchDeck()
        self.assertNotIn(Card("B", "spades"), deck)
