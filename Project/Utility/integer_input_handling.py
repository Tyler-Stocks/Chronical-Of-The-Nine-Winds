from Project.Utility import input_utility, error_messages, error_handling, console_util

inputs        = input_utility.Inpututility()
error         = error_messages.InputErrors()
errorHandling = error_handling.ErrorHandling()
console       = console_util.Console()

class HandleIntegerInput:

    def __init__(self):
        pass

    def user_int_input(self, message: str, lower_bound: int, upper_bound: int) -> int:
        console.clear()

        error_occured: bool = True
        user_input: int = 0

        while error_occured:
            user_input: int     = int(input(f'What is your {message}?\n'))
            error_occured: bool = errorHandling.integer(user_input, lower_bound, upper_bound)
        return int(user_input)

    def get_int_input(self, message: str, lower_bound: int, upper_bound: int) -> int:
        console.clear()

        user_input: int = 0

        while True:
            user_input = self.user_int_input(message, lower_bound, upper_bound)
            if inputs.confirm(user_input):
                break
        return user_input
