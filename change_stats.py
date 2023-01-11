"""Imports a list of stats for the player, to be edited."""
from base_stats import player_base_stats

def change_player_stats(stat_name, new_value):
    """Looks throught the dictionary, to edit the stats."""
    stats = player_base_stats()
    for stat_dict in stats:
        if stat_name in stat_dict:
            stat_dict[stat_name] = new_value
    return stats
