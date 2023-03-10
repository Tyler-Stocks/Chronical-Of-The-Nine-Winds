from Main.Personilization.race_select import Race
from Main.Personilization.name_select import Name

race = Race
name = Name

class ClassSelector():

    def __init__(self) -> None:

        self.classes = ''

        self.race = race
        self.name = name

    def ask_user_class(self) -> str:

        if self.race == 'Human':
            print(f'So {self.name} you are a human. What class would you like to be.\n')

            self.classes = input('''1. Hunter:
                                        You were born and raised in the wild forest of the Nethel Draunest. Living a solitary life with only your parents, and your pet
                                        wolf you don't have much experience with social interaction, and thus tend to be a little bit akward. Many years in the wild have
                                        honed your relflexes, and your sense of perception is heightend as well.

                                        -1 Charisma
                                        +1 Perception
                                        +1 Agility

                                        -----------Starting Armor-----------

                                        -----Hunters Helmet-----                              -----Hunters Coat-----

                                        A simple leather helmet, it provides some defense,    A simple leather Coat, it provides some defense,
                                        and will keep your head warm in a pinch.              and will keep your body warm in a pinch.

                                        Weight: 1.2kg                                         Weight: 2kg
                                        Defense: + 2                                          Defense: + 5
                                        Stealth: + 1                                          Stealth: + 1
                                        Warmth: + 1                                           Warmth: + 3

                                        -----Hunters Trousers-----                            -----Hunters Boots-----

                                        A simple pair of leather trousers, they provide       A simple pair of leather boots, they will provide some protection
                                        some defensive capability, and will keep your legs    for your feet, and will keep them reasonably warm.
                                        reasonably warm.

                                        Weight: 1.6kg                                         Weight: 2.3kg
                                        Defense: + 4                                          Defense: + 3
                                        Stealth: + 1                                          Stealth: + 1
                                        Warmth: + 2                                           Warmth: + 1
                                        
                                        ----------Starting Weapons----------
                                        
                                        -----Hunters Bow-----                                -----Hunters Knife-----
                                        
                                        A simple handmade bow, works well for hunting,       A simple hunting knife. Great for skinning animals, however it is
                                        but is not very equiped for tougher enimies.         not very equiped for peircing armor.
                                        
                                        Weight: 1.1kg                                        Weight: 150g
                                        Attack: 5                                            Attack: 5
                                        Sound: Noisy                                         Sound: Quiet
                                ''')
        else:
            print("hello world")

        return self.classes

Class_Select = ClassSelector()

Class = Class_Select.ask_user_class()
