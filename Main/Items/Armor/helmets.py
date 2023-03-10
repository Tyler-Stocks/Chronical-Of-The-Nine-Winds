# INFO:
#
# Weight is measured in grams
# All atributes listed in the line below are required, if it is not applicable set the value to false or zero.
# Order of attributes should be: {Name, Class, Type, Rarity, Weight, Arcane, Defense Type, Defense, Elemental Resist, Stealth, Warmth, Other}

class Helmets():

    def __init__(self) -> None:
        pass

    def helmets(self) -> dict:

        hunters_helmet = {'Name': 'Hunters Helmet', 'Class': 'Armor', 'Type': 'Helmet', 'Rarity': 'Common', 'Weight': 1000, 'Arcane': False,
                          'Defense Type': 'Physical', 'Defense': 10, 'Elemental Resist': False, 'Stealth': 1, 'Warmth': 1
                        }

        return hunters_helmet
