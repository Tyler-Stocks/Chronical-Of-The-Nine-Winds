from race_select import MainRaceSelect as race
from name_select import MainNameSelect as name

class MainClassSelect():

    class ClassSelect():

        def __init__(self):
            
            self.proffesion = ''

            self.race = race.Race
            self.name = name.Name

        def ask_user_proffesion(self):

            if self.race == 'Human':
                print(f'So {self.name} you are a human. What class would you like to be.\n')

                classSelect = input(f'''1. Hunter: 
                                            You were born and raised in the wild forest of the Nethel Draunest. Living a solitary life with only your parents, and your pet
                                            wolf you don't have much experience with social interaction, and thus tend to be a little bit akward. Many years in the wild have
                                            honed your relflexes, and your sense of perception is heightend as well. 

                                            -1 Charisma
                                            +1 Perception
                                            +1 Agility

                                                               -----------Starting Equipment-----------
                                            
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
                                    ''')
                