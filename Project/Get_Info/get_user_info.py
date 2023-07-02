import json
from Project.Utility import integer_input_handling, string_input_handling

integer = integer_input_handling.HandleIntegerInput()
string = string_input_handling.HandleStringInput()

def get_age() -> None:
    age_information: dict[str, int] = {'Age': integer.get_int_input('How old are you?', 0, 110)}
    with open('data/age_data.json', 'w') as f:
        f.write(json.dumps(age_information, indent = 4))

def get_gender() -> None:
        gender_information = {
            'Gender' : string.get_str_input('What is your gender?', 20).capitalize(),
            'First Pronoun' : string.get_str_input('What is your first pronoun?', 10).capitalize(),
            'Second Pronoun' : string.get_str_input('What is your second pronoun?', 10).capitalize(),
        }
        with open('data/gender_data.json', 'w') as f:
            f.write(json.dumps(gender_information, indent = 4))

def get_name() -> None:
        name_information = {
            'First Name'  : string.get_str_input('What is your first name?', 50).capitalize(),
            'Middle Name' : string.get_str_input('What is your middle name?', 50).capitalize(),
            'Last Name'   : string.get_str_input('What is your last name?', 50).capitalize(),
        }
        with open('data/name_data.json', 'w') as f:
            f.write(json.dumps(name_information, indent = 4))

def main() -> None:
    get_age()
    get_name()
    get_gender()

main()