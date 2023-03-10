from Main.Personilization.race_select import Race
from Main.Personilization.name_select import Name

name = Name
race = Race

class AgeSelector():

    def __init__(self):

        self.name = name
        self.race = race

    def ask_user_age(self) -> float:

        while True:

            age_input = float(input(f'So {self.name} how old are you?\n'))

            try:

                if self.race.lower() == 'human' and age_input >= 100:
                    print(f'{self.name} please enter an age less than or equal to 100.\n')

                elif self.race.lower() == 'elf' and age_input >= 500:
                    print(f'{self.name} Please enter an age less than or equal to 500.\n')

                elif self.race.lower() == "dwarf" and age_input >= 250:
                    print(f'{self.name} please enter an age less than or equal to 250.\n')

                elif self.race.lower() == 'giant' and age_input >= 1000:
                    print(f'{self.name} please enter an age less than or equal to 1000.\n')

                else:
                    age_confirmation = input(f'So you are {age_input}.')

                    try:

                        if age_confirmation.lower() in ('yes', 'y'):
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

            except ValueError as exc:
                raise ValueError from exc

        return age_input

Age_Select = AgeSelector()

Age = Age_Select.ask_user_age()
