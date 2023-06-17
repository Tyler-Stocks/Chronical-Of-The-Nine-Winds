from utility import input_utility, console_utility, error_handling, error_messages

inputs = input_utility.InputUtility()
error = error_messages.InputErrors()
errorHandling = error_handling.ErrorHandling()
console = console_utility.Console()

class HandleStringInput:

    def __init__(self) -> None:
        pass

    def user_str_input(self, message: str, max_len: int) -> str:
        console.clear()

        error_occured = True
        user_input = ''

        while error_occured:
            user_input = input(f'What is your {message}?\n')
            error_occured = errorHandling.string(user_input, max_len)
        return user_input

    def get_str_input(self, message: str, max_len: int) -> str:
        console.clear()

        user_input = ''

        while True:
            user_input = self.user_str_input(message, max_len)
            if inputs.confirm(user_input):
                break
        return user_input
