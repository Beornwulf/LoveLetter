class Card():
    """Defines aspects common to all cards."""
    value = None


class Princess(Card):
    """The princess card."""
    value = 8
    cardname = "Princess"


class Countess(Card):
    """The countess card."""
    value = 7
    cardname = "Countess"


class King(Card):
    """The King card."""
    value = 6
    cardname = "King"


class Prince(Card):
    """The prince card."""
    value = 5
    cardname = "Prince"


class Handmaiden(Card):
    """The handmaiden card."""
    value = 4
    cardname = "Handmaiden"


class Baron(Card):
    """The baron card."""
    value = 3
    cardname = "Baron"


class Priest(Card):
    """The priest card."""
    value = 2
    cardname = "Priest"


class Guard(Card):
    """The guard card."""
    value = 1
    cardname = "Guard"