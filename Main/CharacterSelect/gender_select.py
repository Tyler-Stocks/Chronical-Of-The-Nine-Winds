from Main.CharacterSelect.name_select import MainNameSelect as Name

name = Name


class GenderSelector():

    def __init__(self):

        self.gender = ''
        self.name = name.Name

    def ask_user_gender(self):

        while True:

            self.gender = input(f'So {self.name} you a boy or a girl?\n')

            try:
                if self.gender.lower() == "boy":
                    pronoun_1 = "he"
                    pronoun_2 = "him"
                    gender_confirmation = input(f'So {self.name} you are a boy?')

                    try:

                        if gender_confirmation.lower() != "no":
                            print('It will be noted.\n')
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif self.gender.lower() == 'girl':
                    pronoun_1 = 'she'
                    pronoun_2 = 'her'
                    gender_confirmation = input(f'So {self.name} you are a girl?\n')

                    try:

                        if gender_confirmation.lower() != 'no':
                            print('It will be noted.\n')
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif self.gender.isspace():
                    print('Please enter a valid gender.\n')

                else:
                    print('Please enter a valid gender.\n')

            except ValueError as exc:
                raise ValueError from exc

        return self.gender, pronoun_1, pronoun_2

gender_select_obj = GenderSelector()

gender = gender_select_obj.ask_user_gender()
