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
            error_occured = errorHandling.string(self.first_name, 20)

    def get_first_name(self):
        console.clear()

        while True:
            self.input_first_name()
            if inputHandling.confirmation(self.first_name, 'First name'):
                break

        return self.first_name

    def input_middle_name(self):
        console.clear()
        error_occured = True

        while error_occured:
            self.middle_name = input('Please input your middle Name. If you don\'t have a middle name press enter. ')
            error_occured = errorHandling.integer(self.middle_name, 100, 100)

    def get_middle_name(self):
        console.clear()

        while True:
            self.input_middle_name()
            if inputHandling.confirmation(self.middle_name, 'Middle Name'):
                break

        return self.middle_name

    def input_last_name(self):
        console.clear()

        error_occured = True

        while error_occured:
            self.last_name = input('Please input your last name: ')

            error_occured = errorHandling.string(self.last_name, 100)

    def get_last_name(self):
        console.clear()
        while True:
            self.input_last_name()
            if inputHandling.confirmation(self.last_name, 'Last Name'):
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
Name_Instance.get_full_name()
