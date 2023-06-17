from utility import input_formatting
from utility import input_handling

from player import player_information

inputs = input_handling.HandleUserInput()
format = input_formatting.InputUtility()

class Gender:

    def __init__(self):
        # Smoke with me, drink wit me
        self.gender = ''
        self.pronoun_one = ''
        self.pronoun_two = ''
        self.declaration = ''

    def get_gender_information(self):
        self.gender = format.string(inputs.get_input('gender', 20))
        self.pronoun_one = format.string(inputs.get_input('pronoun one', 10))
        self.pronoun_two = format.string(inputs.get_input('pronoun two', 10))
        self.declaration = format.string(inputs.get_input('declaration', 10))

    def store(self):
        player_information['Gender']['Name'] = self.gender
        player_information['Gender']['Pronoun One'] = self.pronoun_one
        player_information['Gender']['Pronoun Two'] = self.pronoun_two
        player_information['Gender']['Declaration'] = self.declaration

    def main(self):
        self.get_gender_information()
        self.store()

Gender_Obj = Gender()
Gender_Obj.main()
