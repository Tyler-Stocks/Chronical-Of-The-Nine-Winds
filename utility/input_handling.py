import keyboard as k

from utility import console as Console
from utility import input_values

console = Console.Console()
inputValues = input_values.InputValues()

class HandleUserInput:

    def __init__(self) -> None:
        # Fucked up liver with some bad kidneys(oh, oh, oh)
        pass

    def invalid_input(self, message: str, is_binary: bool = False) -> None:
        if is_binary:
            print('Input must be "Yes", or "No".')
            console.clear(1)
        elif not is_binary:
            print(f'{message}')
            console.clear(1)

    def check_for_valid_input(self, user_input: str | int | float, valid_input_values: tuple[str, str], message: str) -> bool:
        console.clear()
        if user_input in(valid_input_values):
            return True
        else:
            self.invalid_input(message)
            return False

    def confirmation(self, user_input, message, white_space_is_valid = False):
        console.clear()

        if not white_space_is_valid:
            while True:
                self.confirm = input(f'{user_input} is correct (Y/N)? ')

                if k.is_pressed('y'):
                    return True
                elif k.is_pressed('n'):
                    return False
                else:
                    self.invalid_input(self.confirm, True)
                    return False
        else:
            while True:
                self.confirm = input(f'You don\'t have a {message}? ')

                if k.is_pressed('y'):
                    return True
                elif k.is_pressed('n'):
                    return False
                else:
                    self.invalid_input(self.confirm, True)

    def get_input(self, message: str) -> str:
        console.clear()