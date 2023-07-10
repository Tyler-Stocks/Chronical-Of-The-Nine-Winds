from Project.Utility import console_util

console = console_util.Console()

class InputErrors:

    def __init__(self):
        pass

    def length(self, length: int | float) -> None:
        print(console.color(f'Error! Input cannot be longer than {length}.', 255, 0, 0))
        console.clear(2)

    def type(self, message: str) -> None:
        print(console.color(f'{message}', 255, 0, 0))
        console.clear(2)

    def whitespace(self) -> None:
        print(console.color('Error! Must Provide Input.', 255, 0, 0))
        console.clear(2)

    def range(self, low_bound: int | float, high_bound: int | float) -> None:
        print(console.color(f'Error! input must be in range {low_bound} - {high_bound}.', 255, 0, 0))
        console.clear(2)

    def invalid_binary_input(self, message: str) -> None:
        print(console.color('Input must be Yes or No.'), 255, 0, 0)
        console.clear(2)

    def invalid_input(self, message: str) -> None:
        print(console.color(f'{message}.'), 255, 0, 0)
        console.clear(2)
