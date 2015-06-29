#!/usr/bin/python

import random

class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __str__(self):
        return "%s of %s" % (Card.suit_names[self.suit], 
                             Card.rank_names[self.rank])

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = self.suit, self.rank
        return cmp(t1, t2)

"""Longer version of __cmp__
    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1

        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1

        return 0
"""

class Deck(object):

    def __init__(self):
        self.cards = []
        for suit in range(0, 4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)
    
    def pop_card(self):
        self.cards.pop()

    def add_card(self, card):
        self.cards.add(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort_card(self):
        self.cards.sort()

    def move_card(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_card(self, hand_counts, card_counts):
        hands = []
        for i in range(hand_counts):
            hands[i] = Hand()
            self.move_card(hands[i], card_counts)


class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=""):
        self.cards = []
        self.label = label


pets = Deck()
pets.shuffle()
print "Shuffled cards:"
print pets
print "\n"
print "Deal 5 cards to 5 players:"
pets.deal_card(5, 5)
print pets
