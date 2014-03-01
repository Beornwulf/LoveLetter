from Players import player
import deck
from random import choice

class Game():
    """
    Handles the primary gameplay.
    """
    playerList = []
    
    def __init__(self, size):
        self.players(size)
        self.round = 0
        self.deck = deck.Deck()
        self.deck.shufflecards()
        self.firstPlayer = choice(self.playerList)
    
    def players(self, size):
        """
        Generates the required number of player instances, currently with automatic names.
        """
        playernumber = 0
        while len(self.playerList) < size:
            playernumber += 1
            playername = "Player " + str(playernumber)
            newPlayer = player.Player(playername)
            self.playerList.append(newPlayer)
    
    def print_game_status(self):
        """
        Prints the current status of the game, the deck, and all the players
        """
        self.deck.print_deck()
        self.deck.print_sideboard()
        for i in self.playerList:
            i.print_player()
            