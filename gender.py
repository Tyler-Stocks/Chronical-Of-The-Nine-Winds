from utility import console as Console
from utility import input_formatting
from utility import error_handling
from utility import input_handling

from player import player_information

inputs = input_handling.HandleUserInput()
format = input_formatting.InputUtility()
console = Console.Console()
errors = error_handling.ErrorHandling()

class Gender:

    def __init__(self):
        # Smoke with me, drink wit me
        self.gender = ''
        self.pronoun_one = ''
        self.pronoun_two = ''
        self.declaration = ''

    def get_gender(self) -> str:
        console.clear()

        while True:
            self.gender = inputs.user_input('gender', 20)
            if inputs.confirmation(self.gender):
                break
        return self.gender

    def get_first_pronoun(self) -> str:
        console.clear()

        while True:
            self.pronoun_one = inputs.user_input('first pronoun', 20)
            if inputs.confirmation(self.pronoun_one):
                break
        return self.pronoun_one

    def get_second_pronoun(self) -> str:
        console.clear()

        while True:
            self.pronoun_two = inputs.user_input('second pronoun', 20)
            if inputs.confirmation(self.pronoun_two):
                break
        return self.pronoun_two

    def get_declaration(self) -> str:
        console.clear()

        while True:
            self.declaration = inputs.user_input('declaration', 10)
            if inputs.confirmation(self.declaration):
                break
        return self.declaration

    def get_gender_information(self):
        self.get_gender()
        self.get_first_pronoun()
        self.get_second_pronoun()
        self.get_declaration()

    def format(self):
        format.string(self.gender)
        format.string(self.pronoun_one)
        format.string(self.pronoun_two)
        format.string(self.declaration)
