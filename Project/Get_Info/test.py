import json
from Project.Utility import integer_input_handling, string_input_handling

integer = integer_input_handling.HandleIntegerInput()
string = string_input_handling.HandleStringInput()

class Get_Info:
    def __init__(self):
        pass

    def get_age(self) -> str:
        return json.dumps({'Age': integer.get_int_input('How old are you?', 0, 110)}, indent = 4)

    def get_gender(self) -> str:
        return json.dumps({
            'Gender': string.get_str_input('What is your gender?', 20).capitalize(),
            'First Pronoun': string.get_str_input('What is your first pronoun?', 10).capitalize(),
            'Second Pronoun': string.get_str_input('What is your second pronoun?', 10).capitalize(),
            }, indent = 4)

    def get_name(self) -> str:
        return json.dumps({
            'First Name': string.get_str_input('What is your first name?', 50).capitalize(),
            'Middle Name': string.get_str_input('What is your middle name?', 50).capitalize(),
            'Last Name': string.get_str_input('What is your last name?', 50).capitalize(),
            }, indent = 4)

    def main(self) -> None:
        with open('data/user_info.json') as f:
            f.write(self.get_age())
            f.write(self.get_gender())
            f.write(self.get_name())

Get_Info().main()