import json
import Main.utility.string_input_handling

inputs = Main.utility.string_input_handling.HandleStringInput()

class Gender:

    def __init__(self):
        self.gender = ''
        self.pronoun_one = ''
        self.pronoun_two = ''
        self.declaration = ''

    def get_gender_information(self):
        self.gender = inputs.get_str_input('gender', 20).capitalize()
        self.pronoun_one = inputs.get_str_input('first pronoun', 10).capitalize()
        self.pronoun_two = inputs.get_str_input('second pronoun', 10).capitalize()
        self.declaration = inputs.get_str_input('declaration', 10).capitalize()

    def format_gender(self) -> str:
        gender_information = {
            'Gender': f'{self.gender}',
            'First Pronoun': f'{self.pronoun_one}',
            'Second Pronoun': f'{self.pronoun_two}',
            'Declaration': f'{self.declaration}',
            'Gender Length': f'{len(self.gender.strip())}'
        }
        gender_data = json.dumps(gender_information, indent = 4)
        return gender_data

    def save(self):
        with open('data/data.json', 'w') as f:
            f.write(self.format_gender())

    def main(self):
        self.get_gender_information()

Gender_Obj = Gender()
Gender_Obj.main()
