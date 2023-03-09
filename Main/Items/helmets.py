# INFO:
#
# Weight is measured in grams
# All atributes listed in the line below are required, if it is not applicable set the value to false or zero.
# Order of attributes should be: {Name: QTY, Class, Type, Rarity, Weight, Arcane, Defense, Magic Defense, Elemental Resist, Stealth, Warmth, Other}

class Helmets():

    def __init__(self) -> None:
        pass

    def helmets(self):

        hunters_helmet = {'Hunters Helmet': 1, 'Class': 'Armor', 'Type': 'Helmet', 'Rarity': 'Common', 'Weight': 1000, 'Arcane': False,
                         'Defense': 10, 'Magic Defense': False, 'Elemental Resist': False, 'Stealth': 1, 'Warmth': 1
                        }
