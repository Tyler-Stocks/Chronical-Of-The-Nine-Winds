from utility import console as Console
from utility import input_formatting
from utility import error_handling
from utility import input_handling

from player import player_information

inputs = input_handling.HandleUserInput()
errorHandling = error_handling.ErrorHandling()
format = input_formatting.InputUtility()
console = Console.Console()

class Name:
    def __init__(self):
        # Fucked Up liver, wit some bad kidneys(oh, oh, oh)
        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.full_name = ''

    def get_first_name(self):
        console.clear()

        while True:
            self.first_name = inputs.user_input('first name', 50)
            if inputs.confirmation(self.first_name):
                break
        return self.first_name

    def get_middle_name(self):
        console.clear()

        while True:
            self.middle_name = inputs.user_input('middle name', 50)
            if inputs.confirmation(self.middle_name):
                break
        return self.middle_name

    def get_last_name(self):
        console.clear()
        while True:
            self.last_name = inputs.user_input('last name', 50)
            if inputs.confirmation(self.last_name):
                break
        return self.last_name

    def get_full_name(self):
        self.first_name = format.string(self.get_first_name())
        self.middle_name = format.string(self.get_middle_name())
        self.last_name = format.string(self.get_last_name())

        self.full_name = f'{self.first_name.capitalize()} {self.middle_name.capitalize()} {self.last_name.capitalize()}'

    def store(self):
        player_information['Name']['First Name'] = self.first_name
        player_information['Name']['Middle Name'] = self.middle_name
        player_information['Name']['Last Name'] = self.last_name
        player_information['Name']['Full Name'] = self.full_name

    def main(self):
        console.clear()
        self.get_full_name()
        self.store()
        print(self.full_name)

Name_Instance = Name()
Name_Instance.main()
