# character.py


class Character(object):
    """
    This is the base class for both Player and Non-Player characters, i.e enemies and heroes.
    """
    def __init__(self, name, factor=None):
        # super(Character, self).__init__()
        self.name = name
        self.factor = factor

        self.life = self._life(factor)

    def _life(self, factor):
        if self.factor is None:
            self.factor = 1
        return 100 * self.factor

    # Factors are used to define the life of an enemy, e.g. '0.25' for a weak enemy and 5 for a strong enemy.
    # def characterLife(self, factor=None):
    #     if factor is None:
    #         factor = 1
    #     character_life = 100 * factor
    #     return character_life


class Player(Character):
    """
    This is the base class for the player character.
    """
    inventory = {
        "weapon": "Dull Sword",
        "armor": "Leather Armor",
        "boots": "Leather Boots",
        "keys": None
    }

#    life = Character.characterLife()


# class Zombie(Character):
#     """
#     This is the base class for Zombies thoughout the game.
#     """

#     def characterLife(self, factor):
#         super(Player, self).characterLife()

#     life = characterLife(.1)


# class Dwarf(Character):
#     """
#     This is the base class for Dwarves thoughout the game.
#     """

#     def characterLife(self, factor):
#         super(Player, self).characterLife()

#     life = characterLife(.5)


# class Dragon(Character):
#     """
#     This is the base class for Dragons thoughout the game.
#     """

#     def characterLife(self, factor):
#         super(Player, self).characterLife()

#     life = characterLife(3)
