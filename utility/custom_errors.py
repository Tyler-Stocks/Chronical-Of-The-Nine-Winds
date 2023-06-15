from utility import console as util

console = util.Console()

class InputErrors:

    def __init__(self):
        # Will I die tonight? I don't know, is it over?
        pass

    def length(self, length: int | float):
        print(console.color_text(f'Error! Input cannot be longer than {length}.'), 255, 0, 0)
        console.clear(2)

    def type(self, data_type: str):
        if data_type.lower() == 'str':
            print(console.color_text('Error! Input must be alphabetical.', 255, 0, 0))
            console.clear(2)
        elif data_type.lower() in ('int', 'float'):
            print(console.color_text('Error! Input must be a real number.', 255, 0, 0))
            console.clear(2)
        elif data_type.lower() == 'bool':
            print(console.color_text('Error! Input must be True or False.', 255, 0, 0))
            console.clear(2)
        else:
            print(console.color_text('Error! Input is invalid type.'), 255, 0, 0)

    def whitespace(self):
        print(console.color_text('Error! Must Provide Input.', 255, 0, 0))
        console.clear(1)

    def range(self, low_bound: int | float, high_bound: int | float):
        print(console.color_text(f'Error! input must be in range {low_bound} - {high_bound}.', 255, 0, 0))
        console.clear(1)
