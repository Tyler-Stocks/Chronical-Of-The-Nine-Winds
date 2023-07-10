from Project.Utility import input_utility, error_messages, error_handling, console_util

inputs = input_utility.Inpututility()
error = error_messages.InputErrors()
errorHandling = error_handling.ErrorHandling()
console = console_util.Console()

class StrInput:

    def __init__(self) -> None:
        self.user_input = ''

    def inputs(self, message, max_len) -> str:
        console.clear()
        error_occured = True

        while error_occured:
            self.user_input = input(f'{message}\n')
            error_occured = errorHandling.string(self.user_input, max_len)
        return self.user_input

    def get(self, message: str, max_len: int) -> str:
        console.clear()

        while True:
            self.user_input = self.inputs(message, max_len)
            if inputs.confirm(self.user_input):
                break
        return self.user_input
