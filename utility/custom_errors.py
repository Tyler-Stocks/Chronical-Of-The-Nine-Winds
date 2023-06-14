from utility import console as util

console = util.Console()

class InputErrors:

    def __init__(self) -> None:
        # Will I die tonight? I don't know, is it over?
        pass

    def length(self, length: int | float) -> None:
        print(console.color_text(f'Error! Input cannot be longer than {length}.'))
        console.clear(2, 'sec')

    def type(self, data_type: str) -> None:
        if data_type.lower() == 'str':
            print(console.color_text('Error! Input must be alphabetical.', 255, 0, 0))
            console.clear(2, 'sec')
        elif data_type.lower() in ('int', 'float'):
            print(console.color_text('Error! Input must be a real number.', 255, 0, 0))
            console.clear(2, 'sec')
        elif data_type.lower() == 'bool':
            print(console.color_text('Error! Input must be True or False.', 255, 0, 0))
            console.clear(2, 'sec')
        else:
            pass

    def whitespace(self) -> None:
        print(console.color_text('Error! Must Provide Input.', 255, 0, 0))
        console.clear(1)

    def range(self, low_bound: int | float, high_bound: int | float) -> None:
        print(console.color_text(f'Error! input must be in range {low_bound} - {high_bound}.', 255, 0, 0))
        console.clear(1)
