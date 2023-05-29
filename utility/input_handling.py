"""
Handle user inputs.
"""
from utility import console as Console

console = Console.Console()

class HandleUserInput:

    def __init__(self):
        pass

    def invalid_input(self, type, message, is_binary = False):
        """Prints Error if an input is invalid."""
        if is_binary:
            print('Input must be "Yes", or "No".')
            console.clear(1)
        elif not is_binary:
            print(f'{message}')
            console.clear(1)