from baseStats import playerBaseStats ; from currency import currency
from factions import factionsList 

# This functions stores all of the variables needed to run the early game
def varList():
    # This function stores the base stats
    playerBaseStats()
    # This function stores the currency
    currency()
    # This function stores your factions, and your relations to them
    factionsList()
