import random

'''
Classes needed for Black Jack Game
'''

suits = ["\u2663", "\u2665", "\u2666", "\u2660"]
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'K': 10, 'Q': 10, 'A': 11}


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return "[" + self.rank + self.suit + "]"
    
    def __repr__(self):
        return "[" + self.rank + self.suit + "]"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                self.deck.append(Card(suit, rank))
                
    def number_of_decks(self):
        self.deck = (self.deck * 4)
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        singe_card = self.deck.pop()
        return singe_card
    
    def __str__(self):
        return f"{self.deck}"


class Hand:
    def __init__(self, name: str):
        self.name = name
        self.cards = []
        self.count = 0
        self.aces = 0
    
    def draw_card(self, card: Card):
        self.cards.append(card)
        self.count += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def ace(self):
        if self.count > 21:
            while self.count > 21 and self.aces > 0:
                self.count -= 10
                self.aces -= 1
    
    def __str__(self):
        return f"{self.name},{self.cards}, {self.count}"
