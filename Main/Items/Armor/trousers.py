# INFO:
#
# Weight is measured in grams
# All atributes listed in the line below are required, if it is not applicable set the value to false or zero.
# Order of attributes should be: {Name, Class, Type, Rarity, Weight, Arcane, Defense Type, Defense, Elemental Resist, Stealth, Warmth, Other}

class Trousers():

    def __init__(self) -> None:
        pass

    def trousers(self) -> dict:

        hunters_trousers = {'Name': 'Hunters Trousers', 'Class': 'Armor', 'Type': 'Coat', 'Rarity': 'Common', 'Weight': 1600, 'Arcane': False,
                            'Defense Type': 'Physical', 'Defense': 4, 'Elemental Resist': False, 'Stealth': 1, 'Warmth': 2
                           }

        return hunters_trousers
