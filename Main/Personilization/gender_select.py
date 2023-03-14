import time

from Main.Personilization.name_select import Name

name = Name

class GenderSelector():

    def __init__(self) -> None:

        self.gender = ''
        self.pronounFirstPerson = ''
        self.pronoun_2 = ''
        self.name = name

    def ask_user_gender(self) -> dict:

        while True:

            self.gender = input('What gender are you?\n')

            try:
                if self.gender.lower() in('boy', 'man', 'male'):
                    self.pronounFirstPerson = "he"
                    self.pronounThirdPerson = "him"
                    gender_confirmation = input(f'So {self.name} you are a boy?')

                    try:

                        if gender_confirmation.lower() != "no":
                            print('It will be noted.\n')
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif self.gender.lower() in('girl', 'woman', 'female'):
                    self.pronounFirstPerson = 'she'
                    self.pronounThirdPerson = 'her'
                    gender_confirmation = input(f'So {self.name} you are a girl?\n')

                    try:

                        if gender_confirmation.lower() != 'no':
                            print('It will be noted.\n')
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif self.gender.lower() not in('boy', 'man', 'male', 'girl', 'woman', 'female'):
                    print('I am to lazy to program in support for more genders, if this offends you')
                    time.sleep(2)
                    print('Perhaps this game is not the one for you. Have a wonderful day, and may god bless you.')

                elif self.gender.isspace():
                    print('You must enter a gender.\n')

                else:
                    print('It appears that something has gone wrong, please try not to use an input of a number as it may cause problems.\n')

            except ValueError as exc:
                raise ValueError from exc

        genderAndPronouns = {'Gender': self.gender, 'Pronoun First Person': self.pronounFirstPerson, 'Pronoun Third Person': self.pronounThirdPerson}

        return genderAndPronouns

Gender_Select = GenderSelector()

Gender = Gender_Select.ask_user_gender()
