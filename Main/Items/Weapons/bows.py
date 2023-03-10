# INFO:
#
# Mass is measured in grams
# All atributes listed in the line below are required, if it is not applicable set the value to false or zero.
# Order of attributes should be: {Name, Class, Type, Rarity, Weight, Arcane, AttackType, Attack, Elemental Damage, Noise}
class Bows():

    def __init__(self) -> None:
        pass

    def bows(self) -> dict:

        huntersBow = {'Name': 'Hunters Bow', 'Class': 'Weapon', 'Type': 'Short Bow', 'Rarity':'Common', 'Weight': 1100,
                      'Arcane': False, 'Attack Type': 'Ranged', 'Attack': 5, 'Elemental Damage': False, 'Noisey': True,
                     }

        return huntersBow