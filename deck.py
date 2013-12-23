from random import shuffle
import card


class Deck():
    """
    Creates and manipulates a deck.
    """

    def __init__(self):
        self.cards = ["princess", "countess", "king", "prince", "prince", "handmaid", "handmaid", "baron", "baron", "priest", "priest", "guard", "guard", "guard", "guard", "guard"]
        self.sideboard = []

    def __str__(self):
        return "The deck contains: \n" + str(self.cards)

    def shufflecards(self):
        """
        Shuffles the deck.
        """
        shuffle(self.cards)

    def set_aside(self, quantity):
        """
        Sets aside a number of cards from the deck until the deck is rebuilt.
        """
        i = 0
        while i < quantity:
            card = self.cards.pop()
            self.sideboard.append(card)
            i += 1

    def draw(self):
        """
        Takes a card from the top of the deck.
        """
        card_drawn = self.cards.pop()
        return card_drawn

    def print_deck(self):
        """
        Prints out the deck , with the top card at the top.
        """
        print("The deck:")
        output = self.cards[::-1]
        for i in output:
            print(i)