# Class to serve as the template for any object with stats, such as the player character, or enemy.
class Stats:
    # Function to define an empty dictionary to be used in other classes, such as the one below.
    def __init__(self):
        self.stats = []

# Class for the player character.
class Player(Stats):
    # Function to define the players base stats
    def __init__(self):
        super().__init__()
        self.stats = [
            {'health': 500, 'defense': 50}, # Defensive Stats
            {'agility': 5, 'stealth': 10}, # Movement Stats
            {'attack': 50, 'critStrength': 75, 'critChance': 0.1, 'stamina': 50}, # Offensive Stats
            {'mana': 100, 'intelligence': 100, 'arcane': 50, 'faith': 100}, # Casting Stats
            {'charisma': 50, 'perception': 10, 'ambushChance': 20, 'luck': 50} # General Stats
        ]
    # Function to change the players base stats
    def change_stat(self, stat:str, value:int):
        for s in self.stats:
            if stat in s:
                s[stat] = value
                return
        # Stat not found
        raise ValueError(f"{stat} not found in Player stats")