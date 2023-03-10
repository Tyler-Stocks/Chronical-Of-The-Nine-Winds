# INFO:
#
# Weight is measured in grams
# All atributes listed in the line below are required, if it is not applicable set the value to false or zero.
# Order of attributes should be: {Name: QTY, Class, Type, Rarity, Weight, Arcane, AttackType, Attack, Elemental Damage, Noise}
class Knives():

    def __init__(self) -> None:

        pass

    def shortKnives(self) -> dict:

        huntersKnife = {'Hunters Knife': 1, 'Class': 'Weapon', 'Type': 'Knife', 'Rarity': 'Common', 'Weight': 1100,
                        'Arcane': False, 'AttackType': 'Physical', 'Attack': 5, 'Elemental Damage': False, 'Noisey': True
                       }

        return huntersKnife
