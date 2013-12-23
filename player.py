class Player():
    def __init__(self, name):
        self.score = 0  # the player's score
        self.newcard = None  # the card that was just drawn
        self.oldcard = None  # the card that is left in the hand after a turn
        self.played = []  # a stack of the cards played thus far, in order
        self.name = name  # name of the player

    def __str__(self):
        return("\nPlayer: " + self.name)

    def print_hand(self):
        if self.hand_size() is 0:
            print("\nHand empty")
        elif self.hand_size() is 1:
            print("\nHand:")
            if not self.newcard is None:
                print(self.newcard.cardname)
            elif not self.oldcard is None:
                print(self.oldcard.cardname)
        else:
            print("\nHand:")
            print(self.oldcard.cardname)
            print(self.newcard.cardname)

    def print_played(self):
        print("\nPlayed:")
        for i in self.played:
            print(i.cardname)

    def hand_size(self):
        size = 0
        if not self.newcard is None:
            size += 1
        if not self.oldcard is None:
            size += 1
        return size

    def get_card(self, deck):
        if not deck:
            print("\nError: Deck is empty.")
        if not self.newcard is None:
            print("\nError: Slot newcard already full with " +
                  self.newcard.cardname)
        else:
            self.newcard = deck.draw()

    def neaten_hand(self):
        if self.oldcard is None:
            if not self.newcard is None:
                self.oldcard = self.newcard
                self.newcard = None

    def discard(self):  # need to add a mechanism to pick a card for this.
        if self.oldcard is None:
            print("\nError: Slot oldcard is empty.")
        else:
            self.played.append(self.oldcard)
            self.oldcard = None
            self.neaten_hand()