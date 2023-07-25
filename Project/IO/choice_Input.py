from Project.Console.format import clear_console

def get_str_choice(
    message: str,
    choices: list[str],
    ) -> str:
    while True:
        clear_console()
        userInput = input(f'{message}\n')
        if userInput.lower() in(choices):
            return userInput
        else:
            print(f'You must choose between {" ".join(choices)}')

def get_int_choice(
    message: str,
    choices: list[int]
    ) -> str:
    clear_console()
    while True:
        userInput = input(f'{message}\n')
        if userInput.lower() in(choices):
            return userInput
        else:
            print(f'You must choose between {" ".join([str(choice) for choice in choices])}')
