"""
Handle user inputs.
Structure:
HandleUserInput
|
|--__init__(self) -> None
|
|--confirmation(self, user_input(str, int, float, bool, list)) -> bool
|
|--invalid_input(self, message(str), is_binary(bool) = False) -> None
|
|--check_for_valid_input(self, user_input(str, int, float), valid_input_values(list), message(str)) -> bool
"""
from utility import console as Console
from utility import input_values

console = Console.Console()
inputValues = input_values.InputValues()

class HandleUserInput:

    def __init__(self) -> None:
        pass

    def confirmation(self, user_input: str | int | float | bool | list) -> bool:
        console.clear()

        while True:
            self.confirm = input(f'{user_input} is correct? ')

            if inputValues.yes_values(self.confirm):
                return True
            if inputValues.no_values(self.confirm):
                return False
            else:
                self.invalid_input('Input must be either "Yes", or "No".', True)

    def invalid_input(self, message: str, is_binary: bool = False) -> None:
        """Prints Error if an input is invalid."""
        if is_binary:
            print('Input must be "Yes", or "No".')
            console.clear(1)
        elif not is_binary:
            print(f'{message}')
            console.clear(1)

    def check_for_valid_input(self, user_input: str | int | float, valid_input_values: list, message: str) -> bool:
        """Check for valid user input."""
        console.clear()
        if user_input in(valid_input_values):
            return True
        else:
            self.invalid_input(message)
            return False