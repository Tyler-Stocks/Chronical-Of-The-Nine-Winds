import json
from Project.Utility import integer_input_handling, string_input_handling, console_util

console = console_util.Console()
integer = integer_input_handling.IntInput()
string = string_input_handling.StrInput()

class Get_User_Info:
    def __init__(self):
        self.age_info = ''
        self.gender_info = ''
        self.name_info = ''
        self.user_info = ''

    def age(self) -> str:
        self.age_info = json.dumps({'Age': integer.get('How old are you?', 0, 110)})
        return self.age_info

    def gender(self) -> str:
        self.gender_info = json.dumps({
            'Gender': string.get('What is your gender?', 20).capitalize(),
            'First Pronoun': string.get('What is your first pronoun?', 10).capitalize(),
            'Second Pronoun': string.get('What is your second pronoun?', 10).capitalize(),
            })
        return self.gender_info

    def name(self) -> str:
        self.name_info = json.dumps({
            'First Name': string.get('What is your first name?', 50).capitalize(),
            'Middle Name': string.get('What is your middle name?', 50).capitalize(),
            'Last Name': string.get('What is your last name?', 50).capitalize(),
            })
        return self.name_info

    def format(self) -> None:
        self.user_info = json.dumps({
            'Name Information': self.name_info,
            'Gender Information': self.gender_info,
            'Age Information': self.age_info,
        })

    def store(self) -> None:
        with open('data/data.json', 'w') as f:
            f.write(self.user_info)
            f.close()

    def main(self) -> None:
        self.age()
        self.name()
        self.gender()
        self.format()
        self.store()
        console.clear()

Get_User_Info().main()