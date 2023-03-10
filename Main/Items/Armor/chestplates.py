# INFO:
#
# Weight is measured in grams
# All atributes listed are requried, if a value is not applicable set it to False
# Order of attributes should be: {Name, Class, Type, Rarity, Weight, Arcane, Defense Type, Defense, Elemental Resist, Stealth, Warmth, Other}

class Chestplates():

    def __init__(self) -> None:

        pass

    def coats(self) -> dict:

        hunters_coat = {'Name': 'Hunters Coat', 'Class': 'Armor', 'Type': 'Coat', 'Rarity': 'Common', 'Weight': 2000, 'Arcane': False,
                       'Defense Type': 'Physical', 'Defense': 5, 'Elemental Resist': False, 'Stealth': 1, 'Warmth': 1
                       }

        return hunters_coat
