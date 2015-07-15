# character.py

import weapons


class Character(object):
    """
    This is the base class for both Player and Non-Player characters, i.e enemies and heroes.
    To create a character, you need to call the Character class with both a name and a factor to allot the character a certain amount of 'life'. The default factor is 1 and allots 100 life to the Character.
    """
    def __init__(self, name, factor=None):
        # super(Character, self).__init__()
        self.name = name
        self.factor = factor

        self.life = int(self._life(factor))

    def _life(self, factor):
        if self.factor is None:
            self.factor = 1
        return 100 * self.factor


class Player(Character):
    """
    This is the base class for the player character.
    The base Player class gives the Player an inventory.
    """
    inventory = {
        "weapon": weapons.weapons['Dull Sword'],
        "armor": "Leather Armor",
        "boots": "Leather Boots",
        "keys": None
    }

    _type = "PC"


class Zombie(Character):
    """
    This is the base class for Zombies thoughout the game.
    Zombies have a factor of 0.1 giving them 10 life.
    """

    def __init__(self, name, factor=0.1):
        self.name = name
        self.factor = factor
        self.life = int(self._life(factor))

    inventory = {
        "weapon": weapons.weapons['Gnashing Teeth'],
        "item": None
    }

    _type = "NPC"


class Dwarf(Character):
    """
    This is the base class for Dwarves thoughout the game.
    Dwarves have a factor of 0.5 giving them 50 life.
    """

    def __init__(self, name, factor=0.5):
        self.name = name
        self.factor = factor
        self.life = int(self._life(factor))

    inventory = {
        "weapon": weapons.weapons['Dwarfish Sword'],
        "item": None
    }

    _type = "NPC"


class Dragon(Character):
    """
    This is the base class for Dragons thoughout the game.
    Dragons have a factor of 5 giving them 500 life.
    """

    def __init__(self, name, factor=5):
        self.name = name
        self.factor = factor
        self.life = int(self._life(factor))

    inventory = {
        "weapon": weapons.weapons['Dragon Breath'],
        "item": None
    }

    _type = "NPC"
