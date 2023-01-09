#Defines player base stats before class is implemented
def playerBaseStats():
  stats = [   
  # Defensive Stats 
  {'health': 500, 'defense': 50}, 
  # Movement Stats   
  {'agility': 5, 'stealth': 10},
  # Offensive Stats   
  {'attack': 50, 'critStrength': 75, 'critChance': 0.1, 'stamina': 50}, 
  # Casting Stats   
  {'mana': 100, 'intelligence': 100, 'arcane': 50, 'faith': 100}, 
  # General Stats   
  {'charisma': 50, 'perception': 10, 'ambushChance': 20, 'luck': 50}
  ]
  return stats
