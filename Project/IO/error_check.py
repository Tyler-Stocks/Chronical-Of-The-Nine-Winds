from Project.Console.format import clear_console, color_text

def check_string(
    userInput: str,
    minLen: int = 1,
    maxLen: int = 100,
    ) -> bool:

    if not len(userInput.strip()):
        print(color_text('Error! Must Provide Input.', 255, 0, 0))
        clear_console(2)
        return True
    elif not userInput.isalpha():
        print(color_text('Error! Input Must Be Alphabetical.', 255, 0, 0))
        clear_console(2)
        return True
    elif len(userInput) > maxLen:
        print(color_text(f'Error! Input Cannot Be Longer Than {maxLen} Characters.', 255, 0, 0))
        clear_console(2)
        return True
    elif len(userInput) < minLen:
        print(color_text(f'Error! Input Cannot Be Longer Than {minLen} Characters.', 255, 0, 0))
        clear_console(2)
        return True
    return False

def check_integer(
    userInput: str,
    min: int = 0,
    max: int = 1,
    ) -> bool:

    if not len(str(userInput)):
        print(color_text('Error! Must Provide Input.', 255, 0, 0))
        clear_console(2)
        return True
    elif str(userInput).isalpha():
        print(color_text('Error! Input Must Be An Integer.', 255, 0, 0))
        clear_console(2)
        return True
    elif int(userInput) < min:
        print(color_text(f'Error! Input Must be Greater Than {min}.', 255, 0, 0))
        clear_console(2)
        return True
    elif int(userInput) > max:
        print(color_text(f'Error! Input Must Be Less than {max}.', 255, 0, 0))
        clear_console(2)
        return True
    return False