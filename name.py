from Utility import errors as e
from Utility import input_values as iV
from Utility import console as c
from Utility import input_error_handler as iEH
import player as p

playerInformation = p.Player()
inputError = e.InputErrors()
inputs = iV.InputValues()
console = c.Console()
inputErrorHandler = iEH.InputErrorHandler()

class Name:

    def __init__(self):

        self.firstName = ''
        self.middleName = ''
        self.lastName = ''
        self.fullName = ''

        self.confirm = ''

        console.clear(0)

# Get First Name
    def input_first_name(self):
        console.clear(0)

        errorOccured = True

        while errorOccured:
            self.firstName = input('Please input your first name: ')

            errorOccured = inputErrorHandler.input_error_handler(
                self.firstName, 'str', 99)

    def confirm_first_name(self):
        console.clear(0)

        while True:
            self.confirm = input(f'{self.firstName} is correct? ')

            if inputs.yes_values(self.confirm):
                return True
            elif inputs.no_values(self.confirm):
                return False
            else:
                inputError.invalid_input('yes or no')

    def get_first_name(self):
        console.clear(0)

        while not inputs.yes_values(self.confirm):
            self.input_first_name()
            self.confirm_first_name()

        self.confirm = ''
        return self.firstName

# Get Middle Name
    def check_for_middle_name(self):
        console.clear(0)

        while True:
            hasMiddleName = input("Do you have a middle name? ")
            if inputs.yes_values(hasMiddleName):
                return True
            elif inputs.no_values(hasMiddleName):
                return False
            else:
                inputError.invalid_input('yes or no')


    def input_middle_name(self):
        console.clear(0)

        errorOccured = True

        while errorOccured:
            self.middleName = input('Please input your middle name: ')

            errorOccured = inputErrorHandler.input_error_handler(
                self.middleName, 'str', 99)

    def confirm_middle_name(self):
        console.clear(0)

        while True:
            self.confirm = input(f'{self.middleName} is correct? ')

            if inputs.yes_values(self.confirm):
                return True
            elif inputs.no_values(self.confirm):
                return False
            else:
                inputError.invalid_input('yes or no')

    def get_middle_name(self):
        console.clear(0)

        if not self.check_for_middle_name():
            pass
        else:
            while not inputs.yes_values(self.confirm):
                self.input_middle_name()
                self.confirm_middle_name()

        self.confirm = ''
        return self.middleName

# Get Last Name
    def input_last_name(self):
        console.clear(0)

        errorOccured = True

        while errorOccured:
            self.lastName = input('Please input your last name: ')

            errorOccured = inputErrorHandler.input_error_handler(
                self.lastName, 'str', 99)

    def confirm_last_name(self):
        console.clear(0)

        while True:
            self.confirm = input(f'{self.lastName} is correct? ')
            if inputs.yes_values(self.confirm):
                return True
            elif inputs.no_values(self.confirm):
                return False
            else:
                inputError.invalid_input('yes or no')

    def get_last_name(self):
        console.clear(0)

        while not inputs.yes_values(self.confirm):
            self.input_last_name()
            self.confirm_last_name()

        self.confirm = ''
        return self.firstName

# Get Full Name, Format it, then Store it
    def format_name(self):
        self.firstName = self.firstName.capitalize().strip()
        self.middleName = self.middleName.capitalize().strip()
        self.lastName = self.lastName.capitalize().strip()

        self.fullName = f'{self.firstName} {self.middleName if not "" else ""} {self.lastName}'

    def get_full_name(self):
        console.clear(0)

        self.get_first_name()
        self.get_middle_name()
        self.get_last_name()

    def save_name(self):
        playerInformation.name['First Name'] = self.firstName
        playerInformation.name['Middle Name'] = self.middleName
        playerInformation.name['Last Name'] = self.lastName
        playerInformation.name['Full Name'] = self.fullName

    def main(self):
        console.clear(0)

        self.get_full_name()
        self.format_name()
        self.save_name()

Name_Instance = Name()
Name_Instance.main()
