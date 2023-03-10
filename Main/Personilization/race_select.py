import time

from Main.BaseStats.player_stats import BaseStats as Stats
from Main.Personilization.name_select import Name

name = Name
stats = Stats()


class  RaceSelector():

    def __init__(self):

        self.race = ''
        self.name = name

    def ask_user_race(self):

        print('You must now choose of which race your were born into this world\n')

        time.sleep(3)

        print('''1. Human:
                The most common race in all the lands. Humans are not particulariy intelligent, nor are they particullarily physically strong. However, their sheer
                determination to defy all odds as well as their particular knack for negociations has lead to them prospering in the lands or Artaria.

                + 2 Charisma
                + 3 Determination

            2. Dwarf:
                The dwarves are a rare and secretive folk. Hiding away in the Obsidian mountains they craft mechanical, and arcane wonders beyond comprehension. They are much stronger, and
                smarter than the average human. However, they are not nearly as charismatic, and are often found instigating conflicts between other races. Additionally, they are not very
                agaile making them easy targets in combat for more nimble races.

                + 2 Intelect
                + 3 Strength

                - 1 Charisma
                - 3 Agility

            3. Elf:
                Elves are very rarely seen in the lands of Artaria. So rare in fact that they have faded into myth and legend. If myth is to be believed, they are the strongest casters in the land,
                as well as possesing extrodinary intelect, and agility. However, there are many tales of their lack of physicall strenght being their downfall. None have seen the elves in many
                generations, and most human scholars believe they died out in the purge 200 years ago.

                + 3  Mana
                + 10 Casting
                + 5  Intelect
                + 2 Stealth
                + 5 agility

                - 10 Strength
                - 10 Defense
                - 50 Health

            4. Giant:
                Despite the name Giants or Giathrons in their native language are perfectly normal sized. The term giant comes from the elvish word Gianat which means "Those who watch the woods".
                These gental creatures are incredibly skilled in casting arcane magic, a near forgotten art that can be used to directly manipulate the artras of an object. Giants have long since
                left mainland Artaria and live on remote islands where they tend to their crops peacfully living out their long lives.

                + 5  Arcane
                + 5  Strength
                + 10 Magic Defense

                - 5 Stealth\n
        ''')

        while True:

            race_choice = str(input('Which race would you like to pick?\n'))

            try:
                if race_choice.lower() in ('1', 'human'):
                    race_confirmation = str(input(f'So {self.name} you are Human\n'))

                    try:

                        if race_confirmation.lower() in ('yes', 'y'):
                            stats.add('Determination', 3)
                            stats.add('Charisma', 2)
                            self.race = 'Human'
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif race_choice.lower() in ('2', 'Dwarf'):

                    race_confirmation = input(f'so {self.name} you are a dwarf?\n')

                    try:

                        if race_confirmation.lower() in ('yes', 'y'):
                            stats.add('Intelect', 2)
                            stats.add('Strength', 5)
                            stats.add('Agility', -5)
                            stats.add('Charisma', -1)
                            self.race = 'Dwarf'
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif race_choice.lower() in ('3', 'elf'):

                    race_confirmation = str(input(f'So {self.name} you are an Elf?\n'))

                    try:

                        if race_confirmation.lower() in ('yes', 'y'):
                            stats.add('Mana', 3)
                            stats.add('Casting', 10)
                            stats.add('Intelect', 5)
                            stats.add('Stealth', 2)
                            stats.add('Agility', 5)
                            stats.add('Strength', -10)
                            stats.add('Defense', -10)
                            stats.add('Health', -50)
                            self.name = 'Elf'

                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif race_choice.lower() in ('4', 'giant'):
                    race_confirmation = input(f'so {self.name} you are a Giant?\n')

                    try:

                        if race_confirmation.lower() in ('yes', 'y'):
                            stats.add('Arcane', 5)
                            stats.add('Strength', 5)
                            stats.add('Magic Defense', 5)
                            stats.add('Stealth', -5)
                            self.race = 'Giant'
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                else:
                    print('Please enter a valid race.')

            except ValueError as exc:
                raise ValueError from exc

        return self.race

Race_Select = RaceSelector()

Race = Race_Select.ask_user_race()
