from Project.Utility import input_utility, error_messages, error_handling, console_util

inputs = input_utility.Inpututility()
error = error_messages.InputErrors()
errorHandling = error_handling.ErrorHandling()
console = console_util.Console()

class IntInput:

    def __init__(self):
        self.user_input = 0
        self.error_occured = True

    def inputs(self, message, lower_bound, upper_bound) -> int:
        console.clear()

        while self.error_occured:
            self.user_input = int(input(f'{message}\n'))
            self.error_occured = errorHandling.integer(self.user_input, lower_bound, upper_bound)
        return self.user_input

    def get(self, message, lower_bound, upper_bound) -> int:
        console.clear()

        while True:
            self.user_input = self.inputs(message, lower_bound, upper_bound)
            if inputs.confirm(self.user_input):
                break
        return self.user_input
