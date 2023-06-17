import json
from utility import string_input_handling

inputs = string_input_handling.HandleStringInput()

class Name:

    def __init__(self):
        self.first_name = ''
        self.middle_name = ''
        self.last_name = ''
        self.full_name = ''

    def get_name(self):
        self.first_name = inputs.get_str_input('first name', 50).capitalize()
        self.middle_name = inputs.get_str_input('middle name', 50).capitalize()
        self.last_name = inputs.get_str_input('last name', 50).capitalize()
        self.full_name = f'{self.first_name} {self.middle_name} {self.last_name}'

    def format_name(self) -> str:
        name_information = {
            'First Name': f'{self.first_name}',
            'Middle Name': f'{self.middle_name}',
            'Last Name': f'{self.last_name}',
            'Full Name': f'{self.full_name}',
            'Name Length': f'{len(self.full_name.strip())}'
        }
        name_data = json.dumps(name_information, indent = 4)
        return name_data

    def store(self):
        with open('data/data.json', 'w') as f:
            f.write(self.format_name())

    def main(self):
        self.get_name()
        self.store()

Name_Obj = Name()
Name_Obj.main()
