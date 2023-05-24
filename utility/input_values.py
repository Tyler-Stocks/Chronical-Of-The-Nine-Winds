"""
Class to check for input values.
"""
from utility import errors as e
inputs = e.InputErrors()
class InputValues:
    """
    Class to check for certain input values.
    """

    def __init__(self):
        pass

    def yes_values(self, user_input):
        """Return True if input is in 'yes_input_values'"""
        yes_input_values = ['y', 'yes', 'yea', 'yessir',
                            'Y', 'Yes', 'Yea', 'Yessir',
                            'YES', 'YEA', 'YESSIR',
                           ]

        return bool(user_input in(yes_input_values))


    def no_values(self, user_input):
        """Return True if input is in 'no_input_values'"""
        no_input_values = ['n', 'no', 'na', 'nosir',
                           'N', 'No', 'Na', 'Nosir',
                           'NO', 'NA', 'NOSIR',
                          ]

        return bool(user_input in(no_input_values))

    def boy_values(self, user_input):
        """Return True if input is in 'boy_values'"""
        boy_input_values = ['b', 'g', 'boy', 'guy', 'man', 'male',
                            'B', 'G', 'Boy', 'Guy', 'Man', 'Male',
                            'BOY', 'GUY', 'MAN', 'MALE',
                            ]


        return bool(user_input in(boy_input_values))

    def girl_values(self, user_input):
        """Return True if input is in 'girl_values'"""
        girl_input_values = ['f', 'girl', 'gal', 'woman', 'female',
                             'F', 'Girl', 'Gal', 'Woman', 'Female',
                             'GIRL', 'GAL', 'WOMAN', 'FEMALE',
                            ]

        return bool(user_input in(girl_input_values))

    def check_for_yes_no(self, user_input):
        """Checks to see if input is yes or no"""
        while True:
            confirm = input(f'{user_input} is correct? ')

            if self.yes_values(confirm):
                return True
            if self.no_values(confirm):
                return False

            inputs.invalid_input('yes or no')
