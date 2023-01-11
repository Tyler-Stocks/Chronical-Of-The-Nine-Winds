"""This is a list of all of the base stats for various characters in my game."""
# Defines player base stats before class is implemented
def player_base_stats():
    """This is a list of all of the player characters stats, before the class is implemented."""
    stats = [
    {'health': 500, 'defense': 50}, # Defensive Stats
    {'agility': 5, 'stealth': 10}, # Movement Stats
    {'attack': 50, 'critStrength': 75, 'critChance': 0.1, 'stamina': 50}, # Offensive Stats
    {'mana': 100, 'intelligence': 100, 'arcane': 50, 'faith': 100}, # Casting Stats
    {'charisma': 50, 'perception': 10, 'ambushChance': 20, 'luck': 50} # General Stats
    ]
    return stats
