from race_select import MainRaceSelect as race
from name_select import MainNameSelect as name

class age_select():

    def __init__(self):

        self.name = name.Name
        self.race = race.Race

    def ask_user_age(self):

        while True:

            age_input = float(input(f'So {self.name} how old are you?\n'))

            try:

                if self.race.lower() == 'human' and age_input >= 100:
                    print(f'{self.name} please enter an age less than or equal to 100\n')

                elif self.race.lower() == 'elf' and age_input >= 500:
                    print(f'{self.name} Please enter an age less than or equal to 500\n')

                elif self.race.lower() == "dwarf" and age_input >= 250:
                    print(f'{self.name} please enter an age less than or equal to 250\n')

                elif self.race.lower() == 'giant' and age_input >= 1000:
                    print(f'{self.name} please enter an age less than or equal to 1000\n')

                else:
                    age_confirmation = input(f'So you are {age_input}')

                    try:

                        if age_confirmation.lower() in ('yes', 'y'):
                            break

                        else:
                            continue

                    except ValueError:
                        raise ValueError

            except ValueError:
                raise ValueError

        return age_input