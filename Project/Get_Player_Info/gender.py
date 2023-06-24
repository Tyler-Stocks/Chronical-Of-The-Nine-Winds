import json
from Project.Utility import string_input_handling

inputs = string_input_handling.HandleStringInput()

class Gender:

    def __init__(self):
        self.gender:      str = ''
        self.pronoun_one: str = ''
        self.pronoun_two: str = ''
        self.declaration: str = ''

    def get_gender_information(self):
        self.gender:      str = inputs.get_str_input('gender', 20).capitalize()
        self.pronoun_one: str = inputs.get_str_input('first pronoun', 10).capitalize()
        self.pronoun_two: str = inputs.get_str_input('second pronoun', 10).capitalize()
        self.declaration: str = inputs.get_str_input('declaration', 10).capitalize()

    def format_gender(self) -> str:
        gender_information: dict[str, str] = {
            'Gender'         : f'{self.gender}',
            'First Pronoun'  : f'{self.pronoun_one}',
            'Second Pronoun' : f'{self.pronoun_two}',
            'Declaration'    : f'{self.declaration}',
            'Gender Length'  : f'{len(self.gender.strip())}'
        }
        gender_data = json.dumps(gender_information, indent = 4)
        return gender_data

    def store(self) -> None:
        with open('data/gender_data.json', 'w') as f:
            f.write(self.format_gender())

    def main(self) -> None:
        self.get_gender_information()
        self.store()

Gender().main()