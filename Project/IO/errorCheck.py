from Project.Console.format import clearConsole, colorText

def checkString(
    userInput: str,
    minLen: int = 1,
    maxLen: int = 100,
    ) -> bool:

    if not len(userInput.strip()):
        print(colorText('Error! Must Provide Input.', 255, 0, 0))
        clearConsole(2)
        return True
    elif not userInput.isalpha():
        print(colorText('Error! Input Must Be Alphabetical.', 255, 0, 0))
        clearConsole(2)
        return True
    elif len(userInput) > maxLen:
        print(colorText(f'Error! Input Cannot Be Longer Than {maxLen} Characters.', 255, 0, 0))
        clearConsole(2)
        return True
    elif len(userInput) < minLen:
        print(colorText(f'Error! Input Cannot Be Longer Than {minLen} Characters.', 255, 0, 0))
        clearConsole(2)
        return True
    return False

def checkInteger(
    userInput: str,
    min: int = 0,
    max: int = 1,
    ) -> bool:

    if not len(str(userInput)):
        print(colorText('Error! Must Provide Input.', 255, 0, 0))
        clearConsole(2)
        return True
    elif str(userInput).isalpha():
        print(colorText('Error! Input Must Be An Integer.', 255, 0, 0))
        clearConsole(2)
        return True
    elif int(userInput) < min:
        print(colorText(f'Error! Input Must be Greater Than {min}.', 255, 0, 0))
        clearConsole(2)
        return True
    elif int(userInput) > max:
        print(colorText(f'Error! Input Must Be Less than {max}.', 255, 0, 0))
        clearConsole(2)
        return True
    return False