class Player():
    def __init__(self, name):
        self.score = 0  # the player's score
        self.newcard = None  # the card that was just drawn
        self.oldcard = None  # the card that is left in the hand after a turn
        self.played = []  # a stack of the cards played thus far, in order
        self.name = name  # name of the player

    def __str__(self):
        return("\nPlayer: " + self.name)

    def print_player(self):
        print("\nx" + 37 * "-" + "x")
        nameString = "| Player: " + self.name
        while len(nameString) < 38:
            nameString += " "
        nameString += "|"
        print(nameString)
        scoreString = "| Victory Tokens: " + str(self.score)
        while len(scoreString) < 38:
            scoreString += " "
        scoreString += "|"
        print(scoreString)
        self.print_hand()
        self.print_played()
        print("x" + 37 * "-" + "x")
        
    def print_hand(self):
        print("| Hand:" + 31 * " " + "|")
        if self.hand_size() is 0:
            print("|     Empty" + 27 * " " + "|")
        elif self.hand_size() is 1:
            if not self.newcard is None:
                print("|", self.newcard.basic_info(), "|")
            elif not self.oldcard is None:
                print("|", self.oldcard.basic_info(), "|")
        else:
            print("|", self.oldcard.basic_info(), "|")
            print("|", self.newcard.basic_info(), "|")

    def print_played(self):
        print("| Played:" + 29 * " " + "|")
        if not self.played:
            print("|     None" + 28 * " " + "|")
        for i in self.played[::-1]:
            print("|", i.basic_info(), "|")

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
