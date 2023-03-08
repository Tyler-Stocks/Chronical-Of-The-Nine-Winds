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
                                            You were born and raised in the wild forest of the Nethel Draunest

                
                                    ''')
                