from Utility import console as util

console = util.Console()


class InputErrors:

    def __init__(self):
        pass

    def length(self, length):
        print(f'Input cannot be longer than {length}.\n')
        console.clear(1)

    def type(self, dataType):
        if dataType.lower() == 'str':
            print('\nInput must be alphabetic.\n')
            console.clear(1)
        elif dataType.lower() in ('int', 'float'):
            print('Input must be a number.\n')
            console.clear(1)
        elif dataType.lower() == 'bool':
            print('Input must be Trule/False or 1/0.\n')
            console.clear(1)
        else:
            pass

    def whitespace(self):
        print('Must provide input.\n')
        console.clear(1)

    def range(self, lowBound, highBound):
        print(f'Input value must be between {lowBound}, and {highBound}.\n')
        console.clear(1)

    def invalid_input(self, message):
        print(f'The input must be {message}.')
        console.clear(1)
