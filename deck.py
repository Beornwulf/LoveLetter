from random import shuffle
import card


class Deck():
    """
    Creates and manipulates a deck.
    """

    def __init__(self):
        princess = card.Princess()
        countess = card.Countess()
        king = card.King()
        prince1 = card.Prince()
        prince2 = card.Prince()
        handmaiden1 = card.Handmaiden()
        handmaiden2 = card.Handmaiden()
        baron1 = card.Baron()
        baron2 = card.Baron()
        priest1 = card.Priest()
        priest2 = card.Priest()
        guard1 = card.Guard()
        guard2 = card.Guard()
        guard3 = card.Guard()
        guard4 = card.Guard()
        guard5 = card.Guard()
        self.cards = [princess, countess, king, prince1, prince2,
                      handmaiden1, handmaiden2, baron1, baron2, priest1,
                      priest2, guard1, guard2, guard3, guard4, guard5]
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
            aside = self.cards.pop()
            self.sideboard.append(aside)
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
        print("\nx" + 37 * "-" + "x")
        print("| The deck:" + 27 * " " + "|")
        output = self.cards[::-1]
        if not output:
            print("|     Empty" + 27 * " " + "|")
        for i in output:
            print("|", i.basic_info(), "|")
        print("x" + 37 * "-" + "x")

    def print_sideboard(self):
        """
        Prints out the deck , with the top card at the top.
        """
        print("\nx" + 37 * "-" + "x")
        print("| Set aside:" + 26 * " " + "|")
        output = self.sideboard[::-1]
        if not output:
            print("|     Empty" + 27 * " " + "|")
        for i in output:
            print("|", i.basic_info(), "|")
        print("x" + 37 * "-" + "x")