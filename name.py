from utility import errors as e
from utility import input_values as iV
from utility import console as c

from player import player_information

inputs = e.InputErrors()
inputValues = iV.InputValues()
console = c.Console()

class Name:

    def __init__(self):

        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.full_name = ''

        self.confirm = ''

        console.clear(0)

# Get First Name
    def input_first_name(self):
        console.clear(0)

        error_occured = True

        while error_occured:
            self.first_name = input('Please input your first name: ')

            error_occured = inputs.error_handler(self.first_name, 'str', 99)

    def confirm_first_name(self):
        console.clear(0)

        while True:
            self.confirm = input(f'{self.first_name} is correct? ')

            if inputValues.yes_values(self.confirm):
                return True
            elif inputValues.no_values(self.confirm):
                return False
            else:
                inputs.invalid_input('yes or no')

    def get_first_name(self):
        console.clear(0)

        while not inputValues.yes_values(self.confirm):
            self.input_first_name()
            self.confirm_first_name()

        self.confirm = ''
        return self.first_name

# Get Middle Name
    def check_for_middle_name(self):
        console.clear(0)

        while True:
            has_middle_name = input("Do you have a middle name? ")
            if inputValues.yes_values(has_middle_name):
                return True
            elif inputValues.no_values(has_middle_name):
                return False
            else:
                inputs.invalid_input('yes or no')


    def input_middle_name(self):
        console.clear(0)

        error_occured = True

        while error_occured:
            self.middle_name = input('Please input your middle name: ')

            error_occured = inputs.error_handler(self.middle_name, 'str', 99)

    def confirm_middle_name(self):
        console.clear(0)

        while True:
            self.confirm = input(f'{self.middle_name} is correct? ')

            if inputValues.yes_values(self.confirm):
                return True
            elif inputValues.no_values(self.confirm):
                return False
            else:
                inputs.invalid_input('yes or no')

    def get_middle_name(self):
        console.clear(0)

        if not self.check_for_middle_name():
            pass
        else:
            while not inputValues.yes_values(self.confirm):
                self.input_middle_name()
                self.confirm_middle_name()

        self.confirm = ''
        return self.middle_name

# Get Last Name
    def input_last_name(self):
        console.clear(0)

        error_occured = True

        while error_occured:
            self.last_name = input('Please input your last name: ')

            error_occured = inputs.error_handler(
                self.last_name, 'str', 99)

    def confirm_last_name(self):
        console.clear(0)

        while True:
            self.confirm = input(f'{self.last_name} is correct? ')
            if inputValues.yes_values(self.confirm):
                return True
            elif inputValues.no_values(self.confirm):
                return False
            else:
                inputs.invalid_input('yes or no')

    def get_last_name(self):
        console.clear(0)

        while not inputValues.yes_values(self.confirm):
            self.input_last_name()
            self.confirm_last_name()

        self.confirm = ''
        return self.first_name

# Get Full Name, Format it, then Store it
    def format_name(self):
        self.first_name = self.first_name.capitalize().strip()
        self.middle_name = self.middle_name.capitalize().strip()
        self.last_name = self.last_name.capitalize().strip()

        self.full_name = f'{self.first_name} {self.middle_name if not "" else ""} {self.last_name}'

    def get_full_name(self):
        console.clear(0)

        self.get_first_name()
        self.get_middle_name()
        self.get_last_name()

    def save_name(self):
        player_information['Name']['First Name'] = self.first_name
        player_information['Name']['Middle Name'] = self.middle_name
        player_information['Name']['Last Name'] = self.last_name

    def main(self):
        console.clear(0)

        self.get_full_name()
        self.format_name()
        self.save_name()

Name_Instance = Name()
Name_Instance.main()
