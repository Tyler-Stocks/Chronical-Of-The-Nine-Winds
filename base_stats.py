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
            {'Health': 500, 'Defense': 50}, # Defensive Stats
            {'Agility': 5, 'Stealth': 10}, # Movement Stats
            {'Attack': 50, 'critStrength': 75, 'critChance': 0.1, 'Stamina': 50}, # Offensive Stats
            {'Mana': 100, 'Intelligence': 100, 'Arcane': 50, 'Faith': 100}, # Casting Stats
            {'Charisma': 50, 'Perception': 10, 'ambushChance': 20, 'Luck': 50} # General Stats
        ]
    # Function to change the players base stats
    def change_stat(self, stat:str, value:int):
        for s in self.stats:
            if stat in s:
                s[stat] = value
                return
        # Stat not found
        raise ValueError(f"{stat} not found in Player stats")