"""
Get User Name.
Structure
    Name
      |--__init__
      |
      |--input_first_name
      |
      |--confirm_first_name
      |
      |--get_first_name
      |
      |--check_for_middle_name
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
from utility import errors
from utility import input_values
from utility import console as Console
from player import player_information

inputs = errors.InputErrors()
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
        """Input user first name."""
        console.clear(0)
        error_occured = True

        while error_occured:
            self.first_name = input('Input your first Name. ')
            error_occured = inputs.error_handler(
                self.first_name, 'str', 20)

    def confirm_first_name(self):
        """Confirm User First Name."""
        console.clear(0)

        while True:
            self.confirm = input(f'{self.first_name} is correct? ')

            if inputValues.yes_values(self.confirm.lower()):
                return True
            if inputValues.no_values(self.confirm.lower()):
                return False
            else:
                inputs.invalid_input('Input must be either "Yes", or "No".')
                return False


    def get_first_name(self):
        """Get User First Name."""
        console.clear(0)

        while True:
            self.input_first_name()
            if self.confirm_first_name():
                break

    def check_for_middle_name(self):
        """Check to see if user has middle name."""
        console.clear(0)

        while True:
            has_middle_name = input("Do you have a middle name? ")
            if inputValues.yes_values(has_middle_name):
                return True
            if inputValues.no_values(has_middle_name):
                return False

            inputs.invalid_input('yes or no')


    def input_middle_name(self):
        """Input middle name."""
        console.clear(0)

        error_occured = False

        while not error_occured:
            self.middle_name = input('Please input your middle name: ')

            error_occured = inputs.error_handler(
                self.middle_name, 'str', 99)

    def confirm_middle_name(self):
        """Confirm middle name."""
        console.clear(0)

        while True:
            self.confirm = input(f'{self.middle_name} is correct? ')

            if inputValues.yes_values(self.confirm):
                return True
            if inputValues.no_values(self.confirm):
                return False

            inputs.invalid_input('yes or no')

    def get_middle_name(self):
        """Get middle name."""
        console.clear(0)

        if not self.check_for_middle_name():
            pass
        else:
            while not inputValues.yes_values(self.confirm):
                self.input_middle_name()
                self.confirm_middle_name()

        self.confirm = ''
        return self.middle_name

    def input_last_name(self):
        """Input Last Name."""
        console.clear(0)

        error_occured = True

        while error_occured:
            self.last_name = input('Please input your last name: ')

            error_occured = inputs.error_handler(
                self.last_name, 'str', 99)

    def confirm_last_name(self):
        """Confirm Last Name."""
        console.clear(0)

        while True:
            self.confirm = input(f'{self.last_name} is correct? ')
            if inputValues.yes_values(self.confirm):
                return True
            if inputValues.no_values(self.confirm):
                return False

            inputs.invalid_input('yes or no')

    def get_last_name(self):
        """Get Last Name."""
        console.clear(0)

        while not inputValues.yes_values(self.confirm):
            self.input_last_name()
            self.confirm_last_name()

        self.confirm = ''
        return self.first_name

    def format(self):
        """Format Name."""
        self.first_name = self.first_name.capitalize().strip()
        self.middle_name = self.middle_name.capitalize().strip()
        self.last_name = self.last_name.capitalize().strip()

        self.full_name = f'{self.first_name} {self.middle_name if not "" else ""} {self.last_name}'

    def get_full_name(self):
        """Get Full Name."""

        self.get_first_name()
        self.get_middle_name()
        self.get_last_name()

    def store(self):
        """Store Name."""
        player_information['Name']['First Name'] = self.first_name
        player_information['Name']['Middle Name'] = self.middle_name
        player_information['Name']['Last Name'] = self.last_name
        player_information['Name']['Full Name'] = self.full_name

    def main(self):
        """Execute Script"""
        console.clear(0)

        self.get_full_name()
        self.format()
        self.store()

Name_Instance = Name()
Name_Instance.get_full_name()
