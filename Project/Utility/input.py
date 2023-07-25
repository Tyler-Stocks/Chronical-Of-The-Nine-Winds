
from Project.Utility.errorCheck import integer, string
from Project.Utility.console import clearConsole

def confirmInput(userInput: str | int | float) -> bool:
    clearConsole()

    while True:
        confirm: str = input(f'{userInput} is correct(Y/N)?\n').lower()

        if confirm in('y', 'yes'):
            return True
        elif confirm in('n', 'no'):
            return False
        else:
            print('Input must be yes or no.')
            return False

def getInt(message: str, min: int, max: int) -> int:
    confirm: bool = False
    error_occured: bool = True
    userInput: str = '0'

    while error_occured and not confirm:
        clearConsole()
        userInput = input(f'{message}\n')
        error_occured = integer(userInput, min, max)
    return int(userInput)

def getStr(message, min_len, max_len) -> str:
    confirm: bool = False
    error_occured: bool = True
    userInput: str = ''

    while error_occured and not confirm:
       clearConsole()
       userInput = input(f'{message}\n')
       error_occured = string(userInput, min_len, max_len)
       if not error_occured:
        confirmInput(userInput)
       else:
           continue
    return userInput
