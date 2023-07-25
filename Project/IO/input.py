from Project.IO.errorCheck import checkInteger, checkString
from Project.Console.format import clearConsole

def confirmInput(
    userInput: str | int | float,
    ) -> bool:

    while True:
        confirm: str = input(f'{userInput} is correct(Y/N)?\n')
        if confirm.lower() == 'y':
            return True
        elif confirm.lower() == 'n':
            return False
        else:
            print('Input must be yes or no.')

def getInt(
    message: str,
    min: int,
    max: int,
    ) -> int:
    userInput = 0

    while True:
        clearConsole()
        userInput = input(f'{message}\n')
        if checkInteger(userInput, min, max):
            continue
        if confirmInput(userInput):
            break

    return int(userInput)

def getStr(
    message: str,
    min_len: int,
    max_len: int,
    )-> str:
    userInput: str = ''

    while True:
        clearConsole()
        userInput = input(f'{message}\n')
        if checkString(userInput, min_len, max_len):
            continue
        if confirmInput(userInput):
            break

    return userInput