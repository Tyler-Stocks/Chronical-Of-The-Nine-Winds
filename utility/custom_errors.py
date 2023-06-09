from utility import console as util

console = util.Console()

class InputErrors:

    def __init__(self) -> None:
        pass

    def length(self, length: int | float) -> None:
        print(f'Input cannot be longer than {length} characters.\n')
        console.clear(1)

    def type(self, data_type: str) -> None:
        if data_type.lower() == 'str':
            print('Input must be alphabetic.\n')
            console.clear(1)
        elif data_type.lower() in ('int', 'float'):
            print('Input must be a real number.\n')
            console.clear(1)
        elif data_type.lower() == 'bool':
            print('Input must be True or False\n')
            console.clear(1)
        else:
            pass

    def whitespace(self) -> None:
        print('Must provide input.\n')
        console.clear(1)

    def range(self, low_bound: int | float, high_bound: int | float) -> None:
        print(f'Input value must be between {low_bound}, and {high_bound}.\n')
        console.clear(1)
