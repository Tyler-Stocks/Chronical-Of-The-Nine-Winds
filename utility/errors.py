"""
Custom Errors, and Errors Handling
"""
from utility import console as util

console = util.Console()


class InputErrors:
    """
    Handles Input Errors
    """

    def __init__(self):
        pass

    def length_error(self, length):
        """
        Prints Error If Inputed length is too long
        """
        print(f'Input cannot be longer than {length}.\n')
        console.clear(1)

    def type_error(self, data_type):
        """
        Prints Error if the input is of the wrong type
        """
        if data_type.lower() == 'str':
            print('\nInput must be alphabetic.\n')
            console.clear(1)
        elif data_type.lower() in ('int', 'float'):
            print('Input must be a number.\n')
            console.clear(1)
        elif data_type.lower() == 'bool':
            print('Input must be Trule/False or 1/0.\n')
            console.clear(1)
        else:
            pass

    def whitespace_error(self):
        """
        Prints error if there is no input
        """
        print('Must provide input.\n')
        console.clear(1)

    def range_error(self, low_bound, high_bound):
        """
        Prints error if an input if out of range
        """
        print(f'Input value must be between {low_bound}, and {high_bound}.\n')
        console.clear(1)

    def invalid_input(self, message):
        """
        Prints Error if an input is invalid
        """
        print(f'The input must be {message}.')
        console.clear(1)

    def error_handler(self, user_input, data_type, length):
        """Function for custom error handling."""
        error_occured = False

        if len(user_input.strip()) == 0:
            self.whitespace_error()
            error_occured = True
        elif user_input.isnumeric():
            self.type_error(data_type)
            error_occured = True
        elif len(user_input) >= 100:
            self.length_error(length)
            error_occured = True
        else:
            error_occured = False

        return error_occured
