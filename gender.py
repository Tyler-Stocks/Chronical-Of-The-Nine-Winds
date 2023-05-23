from Utility import errors as e
from Utility import input_values as iV
from Utility import console as c
from Utility import input_error_handler as iEH
import player as p

playerInformation = p.Player()
inputError = e.InputErrors()
inputs = iV.InputValues()
console = c.Console()
inputErrorHandler = iEH.InputErrorHandler()


class Gender:

    def __init__(self):

        self.gender = ''
        self.pronounOne = ''
        self.pronounTwo = ''
        self.formalDeclaration = ''

        self.confirm = ''
        self.isValidGender = False

        console.clear(0)

    def input_gender(self):
        console.clear(0)

        errorOccured = True

        while errorOccured:
            self.gender = input('What gender are you? Boy, Girl, or Other: ')

            errorOccured = inputErrorHandler.input_error_handler(self.gender, 'str', 20)

        print(self.gender)

    def check_for_valid_gender(self):
        if inputs.boy_values(self.gender.lower()):
            return True
        elif inputs.girl_values(self.gender.lower()):
            return True
        elif self.gender.lower() == 'other':
            return True
        else:
            return False

    def confirm_gender(self):
        console.clear(0)

        while not self.confirm:
            self.confirm = input(f'{self.gender} is correct? ')


Gender_Instance = Gender()

Gender_Instance.input_gender()
