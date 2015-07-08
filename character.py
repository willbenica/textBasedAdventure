# character.py


class Character(object):
    """
    This is the base class for both Player and Non-Player characters, i.e enemies and heros.
    """
    def __init__(self, name):
        # super(Character, self).__init__()
        self.name = name

    life = 100


class Player(Character):
    """
    This is the base class for the player character.
    """
    pass


class Enemy(Character):
    """
    This is the base class for all enemies thoughout the game.
    """
    pass
