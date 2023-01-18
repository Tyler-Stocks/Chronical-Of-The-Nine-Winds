class Stats:
    def __init__(self):
        self.stats = []
class Player(Stats):
    def __init__(self):
        super().__init__()
        self.stats = [
            {'Health': 500, 'Defense': 50, 'Magic Defense': 10},
            {'Agility': 5, 'Stealth': 10},
            {'Attack': 50, 'critStrength': 75, 'Stamina': 50},
            {'Mana': 100, 'Intelligence': 100, 'Arcane': 50, 'Faith': 100},
            {'Charisma': 50, 'Perception': 10, 'ambushChance': 20, 'Luck': 50},
        ]
    def change_stat(self, stat:str, value:int):
        for s in self.stats:
            if stat in s:
                s[stat] = value
                return
        raise ValueError(f"{stat} not found in Player stats")