# INFO:
#
# Weight is measured in grams
# All atributes listed are requried, if a value is not applicable set it to False
# Order of attributes should be: {Name: QTY, Class, Type, Rarity, Weight, Arcane, Defense, Magic Defense, Elemental Resist, Stealth, Warmth, Other}

class Chestplates():

    def __init__(self) -> None:

        pass

    def coats(self) -> dict:

        hunters_coat = {'Hunters Coat': 1, 'Class': 'Armor', 'Type': 'Coat', 'Rarity': 'Common', 'Weight': 2000, 'Arcane': False,
                       'Def': 5, 'Magic Def': False, 'Elemental Resist': False, 'Stealth': 1, 'Warmth': 1
                      }

        return hunters_coat
