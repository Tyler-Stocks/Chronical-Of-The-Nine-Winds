"""
Module to get the users gender.
"""
from utility import errors as e
from utility import input_values as iV
from utility import console as c

inputs = e.InputErrors()
inputValues = iV.InputValues()
console = c.Console()

class Gender:
    """
    Class to get the users gender
    """

    def __init__(self):

        self.gender = ''
        self.pronoun_one = ''
        self.pronoun_two = ''
        self.formal_declaration = ''

        self.confirm = ''
        self.is_valid_gender = False

        console.clear(0)

    def input_gender(self):
        """
        Have user input their first name
        """
        console.clear(0)

        error_occured = True

        while error_occured:
            self.gender = input('What gender are you? Boy, Girl, or Other: ')

            error_occured = inputs.error_handler(self.gender, 'str', 20)

    def check_for_valid_gender(self):
        """
        Check to see if the user inputed a valid gender
        """
        console.clear(0)

        while True:
            if inputValues.boy_values(self.gender.lower()):
                return True
            if inputValues.girl_values(self.gender.lower()):
                return True
            if self.gender.lower() == 'other':
                return True

            inputs.invalid_input('must be a valid gender')
            return False

    def confirm_gender(self):
        """
        Confirm if the user has inputed the correct gender.
        """
        console.clear(0)


        while True:
            self.confirm = input(f'{self.gender} is correct? ')

            if inputValues.yes_values(self.confirm):
                return True
            if inputValues.no_values(self.confirm):
                return False

            inputs.invalid_input('yes or no')

    def get_custom_gender_name(self):
        """
        If the user chooses 'other', get the name of their 'custom' gender
        """

        while True:
            self.gender = input('Input the name of your gender: ')

            if inputs.error_handler(self.gender, 'str', 25):
                continue


    def get_gender(self):
        """
        Function to get the users gender.
        """
        console.clear(0)

        while True:
            self.input_gender()
            if self.check_for_valid_gender():
                if self.confirm_gender():
                    break

        return self.gender

Gender_Instance = Gender()

Gender_Instance.get_gender()
