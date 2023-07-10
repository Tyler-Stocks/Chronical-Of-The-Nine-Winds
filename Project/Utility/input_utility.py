from Project.Utility import console_util, error_messages

console = console_util.Console()
error   = error_messages.InputErrors()

class Inpututility:

    def __init__(self):
        pass

    def confirm(self, user_input) -> bool:
        console.clear()

        while True:
            confirm = input(f'{user_input} is correct(Y/N)?\n')

            if confirm.lower() in('y', 'yes'):
                return True
            elif confirm.lower() in('n', 'no'):
                return False
            else:
                error.invalid_binary_input(confirm)
                return False

