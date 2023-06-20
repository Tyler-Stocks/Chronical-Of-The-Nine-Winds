import Project.Utility.console_util, Project.Utility.error_messages

console = Project.Utility.console_util.Console()
error   = Project.Utility.error_messages.InputErrors()

class Inpututility:

    def __init__(self):
        pass

    def confirm(self, user_input) -> bool:
        console.clear()

        while True:
            confirm: str = input(f'{user_input} is correct(Y/N)?\n')

            if confirm.lower() == 'y':
                return True
            elif confirm.lower() == 'n':
                return False
            else:
                error.invalid_binary_input(confirm)
                return False

