# INFO:
#
# Weight is measured in grams
# All atributes listed in the line below are required, if it is not applicable set the value to false or zero.
# Order of attributes should be: {Name: QTY, Class, Type, Rarity, Weight, Arcane, Defense, Magic Defense, Elemental Resist, Stealth, Warmth, Other}

class Trousers():

    def __init__(self) -> None:
        pass

    def trousers(self) -> dict:

        hunters_trousers = {'Hunters Trousers': 1, 'Class': 'Armor', 'Type': 'Coat', 'Rarity': 'Common', 'Weight': 1600, 'Arcane': False,
                           'Defense': 4, 'Magic Defense': False, 'Elemental Resist': False, 'Stealth': 1, 'Warmth': 2
                          }

        return hunters_trousers
