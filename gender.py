"""
Module to get the users gender.
Structure:
    Gender
    |
    |--__init__
    |
    |--input_gender
    |
    |--check_for_valid_input
    |
    |--confirm_gender
    |
    |--format
    |
    |--get_gender
"""
from utility import custom_errors as e
from utility import input_values as iV
from utility import console as c
from utility import input_formatting

inputFormat = input_formatting.InputUtility()
inputs = e.InputErrors()
inputValues = iV.InputValues()
console = c.Console()

class Gender:
    """Get, Format, then Store users gender."""

    def __init__(self):

        self.gender = ''
        self.pronoun_one = ''
        self.pronoun_two = ''
        self.declaration = ''
        self.confirm = ''

    def input_gender(self):
        """Have user input their first name"""
        console.clear()

        error_occured = True

        while error_occured:
            self.gender = input('What gender are you? Boy, Girl, or Other: ')
            error_occured = inputs.error_handler(self.gender, 'str', 20)

    def check_for_valid_input(self):
        """Check for valid user input."""
        console.clear()

        while True:
            if inputValues.boy_values(self.gender.lower()):
                self.gender = 'Boy'
                return True
            if inputValues.girl_values(self.gender.lower()):
                self.gender = 'Girl'
                return True
            if self.gender.lower() == 'other':
                self.gender = 'Other'
                return True
            else:
                inputs.invalid_input('Input must be either "Boy", "Girl", or "Other".')
                return False

    def input_custom_gender(self):
        """Have user input custom gender."""
        console.clear()

        error_occured = True

        while error_occured:
            self.gender = input('What is the name of your gender? ')
            error_occured = inputs.error_handler(self.gender, 'str', 20)

    def confirm_gender(self):
        """Confirm gender selection."""
        console.clear()

        while True:
            self.confirm = input(f'{self.gender} is correct? ')

            if inputValues.yes_values(self.confirm):
                return True
            if inputValues.no_values(self.confirm):
                return False
            else:
                inputs.invalid_input('Input must be either "Yes", or "No".')

    def input_first_pronoun(self):
        """Have user input first pronouns."""
        console.clear()

        error_occured = True

        while error_occured:
            self.pronoun_one = input('What is your fist pronoun? ')
            error_occured = inputs.error_handler(self.pronoun_one, 'str', 10)

    def confirm_first_pronoun(self):
        """Confirm first pronoun."""
        console.clear()

        while True:
            self.confirm = input(f'{self.pronoun_one} is correct? ')

            if inputValues.yes_values(self.confirm):
                return True
            if inputValues.no_values(self.confirm):
                return False
            else:
                inputs.invalid_input('Input must be either "yes" or "No.')

    def input_second_pronoun(self):
        """Have user input second pronoun"""
        console.clear()

        error_occured = True

        while error_occured:
            self.pronoun_two = input('What is your second pronoun? ')
            error_occured = inputs.error_handler(self.pronoun_two, 'str', 10)

    def confirm_second_pronoun(self, user_input):
        """Confirm second pronoun"""
        console.clear()

        while True:
            self.confirm = input(f'{user_input} is correct? ')

            if inputValues.yes_values(self.confirm):
                return True
            if inputValues.no_values(self.confirm):
                return False
            else:
                inputs.invalid_input('Input must be either "yes" or "no".')


    def assign_pronouns(self):
        """Assign pronouns based on user input."""
        if self.gender.lower() == 'boy':
            self.pronoun_one = 'He'
            self.pronoun_two = 'Him'
        elif self.gender.lower() == 'girl':
            self.pronoun_one = 'She'
            self.pronoun_two = 'Her'
        else:
            pass

    def get_gender(self):
        """Function to get the users gender."""
        console.clear()

        while True:
            self.input_gender()
            if self.check_for_valid_input():
                if self.confirm_gender():
                    break

    def format(self):
        """Format Gender, and Pronouns"""
        inputFormat.string(self.gender)
        inputFormat.string(self.pronoun_one)
        inputFormat.string(self.pronoun_two)
        inputFormat.string(self.declaration)


Gender_Instance = Gender()
Gender_Instance.get_gender()
