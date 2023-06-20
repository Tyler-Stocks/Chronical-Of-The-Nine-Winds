import Project.Utility.input_utility
import Project.Utility.error_messages
import Project.Utility.error_handling
import Project.Utility.console_util

inputs        = Project.Utility.input_utility.Inpututility()
error         = Project.Utility.error_messages.InputErrors()
errorHandling = Project.Utility.error_handling.ErrorHandling()
console       = Project.Utility.console_util.Console()

class HandleStringInput:

    def __init__(self) -> None:
        pass

    def user_str_input(self, message: str, max_len: int) -> str:
        console.clear()

        error_occured: bool = True
        user_input: str     = ''

        while error_occured:
            user_input: str     = input(f'What is your {message}?\n')
            error_occured: bool = errorHandling.string(user_input, max_len)
        return user_input

    def get_str_input(self, message: str, max_len: int) -> str:
        console.clear()

        user_input: str = ''

        while True:
            user_input: str = self.user_str_input(message, max_len)
            if inputs.confirm(user_input):
                break
        return user_input
