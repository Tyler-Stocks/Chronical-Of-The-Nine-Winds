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
from utility import errors as e
from utility import input_values as iV
from utility import console as c

inputs = e.InputErrors()
inputValues = iV.InputValues()
console = c.Console()

class Gender:
    """Get, Format, then Store users gender."""

    def __init__(self):

        self.gender = ''
        self.pronoun_one = ''
        self.pronoun_two = ''
        self.formal_declaration = ''
        self.confirm = ''

    def input_gender(self):
        """Have user input their first name"""
        console.clear(0)

        error_occured = True

        while error_occured:
            self.gender = input('What gender are you? Boy, Girl, or Other: ')
            error_occured = inputs.error_handler(self.gender, 'str', 20)

    def check_for_valid_input(self):
        """Check for valid user input."""
        console.clear(0)

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

    def confirm_gender(self):
        """Confirm gender selection."""
        console.clear(0)

        while True:
            self.confirm = input(f'{self.gender} is correct? ')

            if inputValues.yes_values(self.confirm.lower()):
                return True
            if inputValues.no_values(self.confirm.lower()):
                return False
            else:
                inputs.invalid_input('Input must be either "Yes", or "No".')

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

    def format(self):
        """Format Gender, and Pronouns"""
        self.gender = self.gender.strip()
        self.pronoun_one = self.pronoun_one.strip()
        self.pronoun_two = self.pronoun_two.strip()
        self.formal_declaration = self.formal_declaration.strip()

    def get_gender(self):
        """Function to get the users gender."""
        console.clear(0)

        while True:
            self.input_gender()
            if self.check_for_valid_input():
                if self.confirm_gender():
                    break

Gender_Instance = Gender()
Gender_Instance.get_gender()
