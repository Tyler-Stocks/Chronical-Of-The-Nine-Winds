from name_select import Name_Select


class gender_select():

    def __init__(self):

        self.gender = ''

    def ask_user_gender(self):

        while True:

                self.gender = input(f'Are you a boy or a girl?\n')

                try:
                    if self.gender.lower() == "boy":

                        pronoun_1 = "he"
                        pronoun_2 = "him"
                        gender_confirmation = str(input(f'So you are a boy?'))

                        try:

                            if gender_confirmation.lower() != "no":

                                break

                            else:

                                continue

                        except ValueError:

                            raise ValueError

                    elif self.gender.lower() == 'girl':

                        pronoun_1 = 'she'
                        pronoun_2 = 'her'
                        gender_confirmation = str(input(f'So you are a girl?'))

                        try:

                            if gender_confirmation.lower() != 'no':

                                break

                            else:

                                continue

                        except ValueError:

                            raise ValueError

                    elif self.gender.isspace():

                        print(f'You must enter your gender.\n')

                    else:

                        print(f'You must enter a valid gender.\n')

                except ValueError:

                    raise ValueError

        return self.gender

gender_select_obj = gender_select()

gender = gender_select_obj.ask_user_gender()