class Card():
    """Defines aspects common to all cards."""
    value = None
    cardname = None


class Princess(Card):
    """The princess card."""
    value = 8
    cardname = "Princess"
    text = "If you discard this card, you are out of the round."


class Countess(Card):
    """The countess card."""
    value = 7
    cardname = "Countess"
    text = ("If you have this card and the King or Prince in your hand, "
            "you must discard this card.")


class King(Card):
    """The King card."""
    value = 6
    cardname = "King"
    text = "Trade hands with another player of your choice."


class Prince(Card):
    """The prince card."""
    value = 5
    cardname = "Prince"
    text = ("Choose any player (including yourself) to discard his or her hand "
            "and draw a new card.")


class Handmaiden(Card):
    """The handmaiden card."""
    value = 4
    cardname = "Handmaiden"
    text = "Until your next turn, ignore all effects from other players' cards."


class Baron(Card):
    """The baron card."""
    value = 3
    cardname = "Baron"
    text = ("You and another player secretly compare hands. "
            "The player with the lower value is out of the round.")


class Priest(Card):
    """The priest card."""
    value = 2
    cardname = "Priest"
    text = "Look at another player's hand."


class Guard(Card):
    """The guard card."""
    value = 1
    cardname = "Guard"
    text = ("Name a non-Guard card and choose another player. "
            "If that player has that card, he or she is out of the round.")