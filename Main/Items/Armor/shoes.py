# INFO:
#
# Weight is measured in grams
# All atributes listed in the line below are required, if it is not applicable set the value to false or zero.
# Order of attributes should be: {Name, Class, Type, Rarity, Weight, Arcane, Defense Type, Defense, Elemental Resist, Stealth, Warmth, Other}

class Shoes():

    def __init__(self) -> None:
        pass

    def boots(self) -> dict:

        hunters_boots = {'Hunters Boots': 1, 'Class': 'Armor', 'Type': 'Boots', 'Rarity': 'Common', 'Weight': 2300, 'Arcane': False,
                        'Defense Type': 'Physical', 'Defense': 3, 'Magic Defense': False, 'Elemental Resist': False, 'Stealth': 1, 'Warmth': 1
                        }

        return hunters_boots
