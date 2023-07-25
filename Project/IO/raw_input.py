from Project.IO.error_check import check_integer, check_string
from Project.IO.confirm import confirm_str, confirm_int
from Project.Console.format import clear_console


def get_int(
    message: str,
    min: int,
    max: int,
    ) -> int:
    userInput = 0

    while True:
        clear_console()
        userInput = input(f'{message}\n')
        if check_integer(userInput, min, max):
            continue
        if confirm_int(int(userInput)):
            break

    return int(userInput)

def get_str(
    message: str,
    min_len: int,
    max_len: int,
    )-> str:
    userInput: str = ''

    while True:
        clear_console()
        userInput = input(f'{message}\n')
        if check_string(userInput, min_len, max_len):
            continue
        if confirm_str(userInput):
            break

    return userInput