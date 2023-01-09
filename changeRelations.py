from factions import factionsList

# This function changes the relation of the faction. This only applies to one item in the 'factions' list
def changeFactionRelation(faction_name, new_relation):
    # Retrieve the list of factions
    factions = factionsList()
    # Find the faction with the matching name
    for faction in factions:
        if faction['name'] == faction_name:
            # Change the relation
            faction['relation'] = new_relation
            break
    # Return the modified list
    return factions

# This function changes the relation of the faction. This applies to all items on the list
def changeFactionRelationAll(new_relation):
    # Retrieve the list of factions
    factions = factionsList()
    # Change the relation for all factions
    for faction in factions:
        faction['relation'] = new_relation
    # Return the modified list
    return factions
