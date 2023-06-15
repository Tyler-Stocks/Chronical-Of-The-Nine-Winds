from utility import input_values
from utility import console as Console
from utility import input_formatting
from utility import error_handling
from utility import input_handling
from player import player_information

inputFormat = input_formatting.InputUtility()
inputValues = input_values.InputValues()
console = Console.Console()
errors = error_handling.ErrorHandling()
inputs = input_handling.HandleUserInput()

class Gender:

    def __init__(self):
        self.gender = ''
        self.pronoun_one = ''
        self.pronoun_two = ''
        self.declaration = ''
        self.confirm = ''

    def input_gender(self) -> str:
        console.clear()
        error_occured = True

        while error_occured:
            self.gender = input('What gender are you? Boy, Girl, or Other: ')
            error_occured = errors.string_error_handler(self.gender, 20)

        return self.gender

    def get_gender(self) -> None:
        console.clear()
        has_confirmed = False

        while has_confirmed:
            self.input_gender

    def input_custom_gender(self) -> str:
        console.clear()

        error_occured = True

        while error_occured:
            self.gender = input('What is the name of your gender? ')
            error_occured = errors.string_error_handler(self.gender, 20)

        return self.gender

    def input_pronouns(self) -> tuple:
        console.clear()
        error_occured = True

        while error_occured:
            self.pronoun_one = input('What is your fist pronoun? ')
            error_occured = errors.string_error_handler(self.pronoun_one, 20)

        console.clear()
        error_occured = True

        while error_occured:
            self.pronoun_two = input('What is your second pronoun? ')
            error_occured = errors.string_error_handler(self.pronoun_two, 20)

        return self.pronoun_one, self.pronoun_two

    def assign_pronouns(self) -> None:
        if self.gender.lower() == 'boy':
            self.pronoun_one = 'He'
            self.pronoun_two = 'Him'
        elif self.gender.lower() == 'girl':
            self.pronoun_one = 'She'
            self.pronoun_two = 'Her'
        else:
            pass

    def format(self) -> None:
        inputFormat.string(self.gender)
        inputFormat.string(self.pronoun_one)
        inputFormat.string(self.pronoun_two)
        inputFormat.string(self.declaration)

    def save(self) -> None:
        player_information['Gender']['Name'] = self.gender
        player_information['Gender']['First Pronoun'] = self.pronoun_one
        player_information['Gender']['Second Pronoun'] = self.pronoun_two


Gender_Instance = Gender()
Gender_Instance.get_gender()
