class Character:
    """The base class for all characters in the game.

    Attributes:
        stats (list): A list of dictionaries containing the various stats for the character.
    """
    def __init__(self):
        """Initializes the Character class and sets the stats attribute as an empty list."""
        self.stats = []

class Player(Character):
    """A class representing a player character in the game.

    Inherits from the Character class and sets the initial stats for the player character.
    """
    def __init__(self):
        """Initializes the Player class and sets the stats attribute using the data from the original function.
        """
        super().__init__()
        self.stats = [
            {'health': 500, 'defense': 50}, # Defensive Stats
            {'agility': 5, 'stealth': 10}, # Movement Stats
            {'attack': 50, 'critStrength': 75, 'critChance': 0.1, 'stamina': 50}, # Offensive Stats
            {'mana': 100, 'intelligence': 100, 'arcane': 50, 'faith': 100}, # Casting Stats
            {'charisma': 50, 'perception': 10, 'ambushChance': 20, 'luck': 50} # General Stats
        ]

    def change_stat(self, stat:str, value:int):
        """Change the value of a stat of a player character.
        Args:
            stat (str): The name of the stat you want to change
            value (int): The value you want to change the stat to
        """
        for s in self.stats:
            if stat in s:
                s[stat] = value
                return
        # Stat not found
        raise ValueError(f"{stat} not found in Player stats")