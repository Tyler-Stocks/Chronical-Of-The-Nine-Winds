from base_stats import player_base_stats
from currency import currency_list
from factions import factions_list

# This functions stores all of the variables needed to run the early game
def varList():
    # This function stores the base stats
    player_base_stats()
    # This function stores the currency
    currency_list()
    # This function stores your factions, and your relations to them
    factions_list()
