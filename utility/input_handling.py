from utility import console as Console
from utility import error_handling
from utility import error_messages

error = error_messages.InputErrors()
errorHandling = error_handling.ErrorHandling()
console = Console.Console()

class HandleUserInput:

    def __init__(self) -> None:
        # Get high with me if you rock with me
        pass

    def check_for_valid_input(self, user_input: str | int | float, valid_input_values: tuple[str, str], message: str) -> bool:
        console.clear()
        if user_input in(valid_input_values):
            return True
        else:
            error.invalid_input(message)
            return False

    def confirmation(self, user_input: str) -> bool:
        console.clear()

        while True:
            confirm = input(f'{user_input} is correct(Y/N)? ')

            if confirm.lower() == 'y':
                return True
            elif confirm.lower() == 'n':
                return False
            else:
                error.invalid_binary_input(confirm)
                return False

    def user_input(self, message: str, max_len: int) -> str:
        console.clear()

        error_occured = True
        user_input = ''

        while error_occured:
            user_input = input(f'Please enter your {message}: ')
            print(user_input)
            error_occured = errorHandling.string(user_input, max_len)
        return user_input

    def get_input(self, message: str, max_len: int) -> str:
        console.clear()

        user_input = ''

        while True:
            user_input = self.user_input(message, 50)
            if self.confirmation(user_input):
                break
        return user_input