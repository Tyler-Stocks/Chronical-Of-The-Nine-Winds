import json
from utility import input_formatting
from utility import input_handling

inputs = input_handling.HandleUserInput()
format = input_formatting.InputUtility()

class Name:
    def __init__(self):
        # Fucked Up liver, wit some bad kidneys(oh, oh, oh)
        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.full_name = ''

    def get_full_name(self):
        self.first_name = format.string(inputs.get_input('first name', 50))
        self.middle_name = format.string(inputs.get_input('middle name', 50))
        self.last_name = format.string(inputs.get_input('last name', 50))
        self.full_name = f'{self.first_name.capitalize()} {self.middle_name.capitalize()} {self.last_name.capitalize()}'

    def store(self):
        

    def main(self):
        self.get_full_name()
        self.store()

Name_Obj = Name()
Name_Obj.main()
