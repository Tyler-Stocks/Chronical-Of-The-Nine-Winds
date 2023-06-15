import keyboard as k

from utility import custom_errors
from utility import input_values
from utility import console as Console
from utility import input_formatting
from utility import error_handling
from utility import input_handling
from player import player_information

inputHandling = input_handling.HandleUserInput()
errorHandling = error_handling.ErrorHandling()
inputFormat = input_formatting.InputUtility()
inputs = custom_errors.InputErrors()
inputValues = input_values.InputValues()
console = Console.Console()

class Name:
    def __init__(self):

        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.full_name = ''
        self.confirm = ''

    def input_first_name(self):
        # Smoke wit me, drink wit me
        console.clear()
        error_occured = True

        while error_occured:
            self.first_name = input('Please input your first Name. ')
            error_occured = errorHandling.string_error_handler(self.first_name, 20)

    def confirm_input(self, user_input, message, white_space_is_valid = False):
        console.clear()

        if not white_space_is_valid:
            while True:
                self.confirm = input(f'{user_input} is correct (Y/N)? ')

                if k.is_pressed('y'):
                    return True
                elif k.is_pressed('n'):
                    return False
                else:
                    inputHandling.invalid_input(self.confirm, True)
                    return False
        else:
            while True:
                self.confirm = input(f'You don\'t have a {message}? ')

                if k.is_pressed('y'):
                    return True
                elif k.is_pressed('n'):
                    return False
                else:
                    inputHandling.invalid_input(self.confirm, True)

    def get_first_name(self):
        console.clear()

        while True:
            self.input_first_name()
            if self.confirm_input(self.first_name, 'First name'):
                break

        return self.first_name

    def input_middle_name(self):
        console.clear()
        error_occured = True

        while error_occured:
            self.middle_name = input('Please input your middle Name. If you don\'t have a middle name press enter. ')
            error_occured = errorHandling.string_error_handler(self.middle_name, 100)

    def confirm_middle_name(self):
        console.clear()

        while True:
            if len(str(self.middle_name)) != 0:
                self.confirm = input(f'{self.middle_name} is correct? ')

                if inputValues.yes_values(self.confirm.lower()):
                    return True
                if inputValues.no_values(self.confirm.lower()):
                    return False
                else:
                    inputHandling.invalid_input(self.confirm, True)
                    return False
            else:
                self.confirm = input('You don\'t have a middle name? ')

                if inputValues.yes_values(self.confirm.lower()):
                    return True
                if inputValues.no_values(self.confirm.lower()):
                    return False
                else:
                    inputHandling.invalid_input(self.confirm, True)
                    return False

    def get_middle_name(self):
        console.clear()

        while True:
            self.input_middle_name()
            if self.confirm_middle_name():
                break

        return self.middle_name

    def input_last_name(self):
        console.clear()

        error_occured = True

        while error_occured:
            self.last_name = input('Please input your last name: ')

            error_occured = errorHandling.string_error_handler(self.last_name, 100)

    def confirm_last_name(self):
        console.clear()
        while True:
            self.confirm = input(f'{self.last_name} is correct? ')
            if inputValues.yes_values(self.confirm):
                return True
            if inputValues.no_values(self.confirm):
                return False
            inputHandling.invalid_input(self.confirm, True)

    def get_last_name(self):
        console.clear()
        while True:
            self.input_last_name()
            if self.confirm_last_name():
                break

        return self.last_name

    def get_full_name(self):
        self.get_first_name()
        self.get_middle_name()
        self.get_last_name()

    def format(self):
        inputFormat.string(self.first_name)
        inputFormat.string(self.middle_name)
        inputFormat.string(self.last_name)

        self.full_name = f'{self.first_name} {self.middle_name if not "" else ""} {self.last_name}'

    def store(self):
        player_information['Name']['First Name'] = self.first_name
        player_information['Name']['Middle Name'] = self.middle_name
        player_information['Name']['Last Name'] = self.last_name
        player_information['Name']['Full Name'] = self.full_name

    def main(self):
        console.clear()
        self.get_full_name()
        self.format()
        self.store()

Name_Instance = Name()
Name_Instance.get_first_name()
