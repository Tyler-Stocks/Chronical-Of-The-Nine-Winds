import time 
class Character_Creation():


    def __init__(self):

        self.gender = ""
        self.name = ""
        self.race = ""
        self.faction = ""
        self.age = 0

    def ask_user_gender(self):

        while True:

                self.name = input(f'Are you a boy or a girl?\n')

                if self.name.lower() == "boy":

                    pronoun_1 = "he"
                    pronoun_2 = "him"
                    gender_confirmation = str(input(f'So you are a boy?'))

                    if gender_confirmation.lower() != "no":

                        break

                    else:

                        continue

                elif self.name.lower() == "girl":

                    pronoun_1 = "she"
                    pronoun_2 = "her"
                    gender_confirmation = str(input(f'So you are a girl?'))

                    if gender_confirmation.lower() != "no":

                        break

                    else:

                        continue

                elif self.name.isspace():

                    print(f'You must enter your gender.\n')

                else:

                    print(f'You must enter a valid gender.\n')


    def ask_user_name(self):

        while True:

                self.name = str(input(f'Hello, what might your name be?\n'))

                if self.name.isspace():
                    print(f'You must enter a name.\n')
                    break

                elif self.name.isnumeric():
                    print(f'You cannot enter a number as your name.\n')

                else:
                    print(f'Something has gone wrong, please enter a valid string as your name.\n')

    def ask_user_race(self):

        print(f'You must now choose of which race your were born into this world\n')

        time.sleep(3)

        

    def ask_user_age(self):

        while True:
            age_input = input(f'So {self.name} how old are you?\n')
            if not age_input.isdigit():
                print("Please enter a valid number.\n")
            else:
                self.age = int(age_input)
                if self.age <= 0 > 120:
                    print("Age must be a positive number.\n")
                else:
                    break

    def character_creatation(self):
        self.ask_user_name()
        self.ask_user_age()

Character_Creation_Obj = Character_Creation()
Character_Creation_Obj.character_creatation()
