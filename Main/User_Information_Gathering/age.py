import json
import Main.Utility.integer_input_handling

inputs = Main.Utility.integer_input_handling.HandleIntegerInput()

class Age:

    def __init__(self):
        self.age = '0'

    def get_age(self):
        self.age = inputs.get_int_input('age', 0, 110)
        return self.age

    def format_age(self) -> str:
        age_information = {
            'Age': f'{self.age}'
        }
        age_data = json.dumps(age_information, indent = 4)
        return age_data

    def store(self):
        with open('data/data.json', 'w') as f:
            f.write(self.format_age())

    def main(self):
        self.get_age()
        self.store()

Age_Obj = Age()
Age_Obj.main()