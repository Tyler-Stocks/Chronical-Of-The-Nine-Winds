"""Import the list of all of the factions"""
from factions import factions_list

# This function changes the relation of the faction.
def change_faction_relation(faction_name, new_relation):
    """Changes the faction relations"""
    # Retrieve the list of factions
    factions = factions_list()
    # Find the faction with the matching name
    for faction in factions:
        if faction['name'] == faction_name:
            # Change the relation
            faction['relation'] = new_relation
            break
    # Return the modified list
    return factions

# This function changes the relation of the faction. This applies to all items on the list
def change_faction_relation_all(new_relation):
    """Changes the relations of all factions"""
    # Retrieve the list of factions
    factions = factions_list()
    # Change the relation for all factions
    for faction in factions:
        faction['relation'] = new_relation
    # Return the modified list
    return factions
