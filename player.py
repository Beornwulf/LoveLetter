import deck


class Player():
    def __init__(self, name):
        self.score = 0  # the player's score
        self.newcard = None  # the card that was just drawn
        self.oldcard = None  # the card that is left in the hand at the end of the turn
        self.played = []  # a stack of the cards played thus far, in order
        self.name = name  # name of the player

    def __str__(self):
        return("Player: " + self.name)

    def print_hand(self):
        print("Hand:\n 1: " + str(self.oldcard) + "\n 2: " + str(self.newcard))

    def print_played(self):
        print("Played:")
        print(self.played)

    def hand_size(self):
        size = 0
        if not self.newcard is None:
            size += 1
        if not self.oldcard is None:
            size += 1
        return size

    def get_card(self, deck):
        if not deck:
            print("Error: Deck is empty.")
        if not self.newcard is None:
            print("Error: Slot newcard already full with " + str(self.newcard))
        else:
            self.newcard = deck.draw()

    def neaten_hand(self):
        if self.oldcard is None:
            if not self.newcard is None:
                self.oldcard = self.newcard
                self.newcard = None

    def discard(self):  # need to add a mechanism to pick a card for this.
        if self.oldcard is None:
            print("Error: Slot oldcard is empty.")
        else:
            self.played.append(self.oldcard)
            self.oldcard = None
            self.neaten_hand()