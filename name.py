"""
Get User Name.
Name
    |--__init__
    |
    |--input_first_name
    |
    |--confirm_first_name
    |
    |--get_first_name
    |
    |--input_middle_name
    |
    |--confirm_middle_name
    |
    |--get_middle_name
    |
    |--input_last_name
    |
    |--confirm_last_name
    |
    |--get_last_name
    |
    |--format
    |
    |--save
    |
    |--main
"""
from utility import custom_errors
from utility import input_values
from utility import console as Console
from utility import input_formatting
from utility import error_handling
from player import player_information

errorHandling = error_handling.ErrorHandling()
inputFormat = input_formatting.InputUtility()
inputs = custom_errors.InputErrors()
inputValues = input_values.InputValues()
console = Console.Console()

class Name:
    """Get, Format, then Save users name based on input."""
    def __init__(self):

        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.full_name = ''
        self.confirm = ''

    def input_first_name(self):
        """Have user input first name."""
        console.clear()
        error_occured = True

        while error_occured:
            self.first_name = input('Please input your first Name. ')
            error_occured = errorHandling.string_error_handler(self.first_name, 20)

    def confirm_input(self, user_input, message, white_space_is_valid = False):
        """Confirm Input Name."""
        console.clear()

        if not white_space_is_valid:
            while True:
                self.confirm = input(f'{user_input} is correct? ')

                if inputValues.yes_values(self.confirm.lower()):
                    return True
                if inputValues.no_values(self.confirm.lower()):
                    return False
                else:
                    inputs.invalid_input('Input must be either "Yes", or "No".')
                    return False
        else:
            while True:
                self.confirm = input(f'You don\'t have a {message}? ')

                if inputValues.yes_values(self.confirm.lower()):
                    return True
                if inputValues.no_values(self.confirm.lower()):
                    return False
                else:
                    inputs.invalid_input('Input must be either "Yes", or "No".')


    def get_first_name(self):
        """Get User First Name."""
        console.clear()

        while True:
            self.input_first_name()
            if self.confirm_input(self.first_name, 'First name'):
                break

        return self.first_name

    def input_middle_name(self):
        """Input middle name."""
        console.clear()
        error_occured = True

        while error_occured:
            self.middle_name = input('Please input your middle Name. If you don\'t have a middle name press enter. ')
            error_occured = inputs.error_handler(self.middle_name, 'str', 20, True)

    def confirm_middle_name(self):
        """Confirm middle name."""
        console.clear()

        while True:
            if len(str(self.middle_name)) != 0:
                self.confirm = input(f'{self.middle_name} is correct? ')

                if inputValues.yes_values(self.confirm.lower()):
                    return True
                if inputValues.no_values(self.confirm.lower()):
                    return False
                else:
                    inputs.invalid_input('Input must be either "Yes", or "No".')
                    return False
            else:
                self.confirm = input('You don\'t have a middle name? ')

                if inputValues.yes_values(self.confirm.lower()):
                    return True
                if inputValues.no_values(self.confirm.lower()):
                    return False
                else:
                    inputs.invalid_input('Input must be either "Yes", or "No".')
                    return False

    def get_middle_name(self):
        """Get middle name."""
        console.clear()

        while True:
            self.input_middle_name()
            if self.confirm_middle_name():
                break

        return self.middle_name

    def input_last_name(self):
        """Input Last Name."""
        console.clear()

        error_occured = True

        while error_occured:
            self.last_name = input('Please input your last name: ')

            error_occured = inputs.error_handler(self.last_name, 'str', 99)

    def confirm_last_name(self):
        """Confirm Last Name."""
        console.clear()

        while True:
            self.confirm = input(f'{self.last_name} is correct? ')
            if inputValues.yes_values(self.confirm):
                return True
            if inputValues.no_values(self.confirm):
                return False

            inputs.invalid_input('yes or no')

    def get_last_name(self):
        """Get Last Name."""
        console.clear()

        while True:
            self.input_last_name()
            if self.confirm_last_name():
                break

        return self.last_name

    def get_full_name(self):
        """Get Full Name."""

        self.get_first_name()
        self.get_middle_name()
        self.get_last_name()

    def format(self):
        """Format Name."""
        inputFormat.string(self.first_name)
        inputFormat.string(self.middle_name)
        inputFormat.string(self.last_name)

        self.full_name = f'{self.first_name} {self.middle_name if not "" else ""} {self.last_name}'

    def store(self):
        """Store Name."""
        player_information['Name']['First Name'] = self.first_name
        player_information['Name']['Middle Name'] = self.middle_name
        player_information['Name']['Last Name'] = self.last_name
        player_information['Name']['Full Name'] = self.full_name

    def main(self):
        """Execute Script."""
        console.clear()

        self.get_full_name()
        self.format()
        self.store()

Name_Instance = Name()
Name_Instance.get_first_name()
