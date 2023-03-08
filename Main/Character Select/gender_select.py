from name_select import MainNameSelect as name


class gender_select():

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

                        except ValueError:
                            raise ValueError

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

                        except ValueError:
                            raise ValueError

                    elif self.gender.isspace():
                        print(f'Please enter a valid gender.\n')

                    else:
                        print(f'Please enter a valid gender.\n')

                except ValueError:
                    raise ValueError

        return self.gender

gender_select_obj = gender_select()

gender = gender_select_obj.ask_user_gender()