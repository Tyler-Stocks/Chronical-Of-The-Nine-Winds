def confirm_str(
    userInput: str,
    ) -> bool:

    while True:
        confirm: str = input(f'{userInput} is correct? (Y/N\n')
        if confirm.lower() in('y', 'yes'):
            return True
        elif confirm.lower() in('n', 'no'):
            return False
        else:
            print('Input must be yes or no.')

def confirm_int(
    userInput: int,
    ) -> bool:

    while True:
        confirm: str = input(f'{userInput} is correct? (Y/N)')
        if confirm.lower() in('y', 'yes'):
            return True
        elif confirm.lower() in('n', 'no'):
            return False
        else:
            print('Input must be yes or no.')
