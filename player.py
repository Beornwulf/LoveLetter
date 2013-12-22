class Player():
    def __init__(self):
        self.score = 0  # the player's score
        self.newcard = None  # the card that was just drawn
        self.oldcard =  # the card that is left in the hand at the end of the turn
        self.played = [] # a stack of the cards played thus far, in order


    def print_hand():
        print("Hand: \n 1: " + str(oldcard) + "\n 2: " + str(newcard))

player1 = Player()