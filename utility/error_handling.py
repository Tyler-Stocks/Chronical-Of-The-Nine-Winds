"""
Class for error handling, and input handling
"""
from utility import custom_errors

error = custom_errors.InputErrors()

class ErrorHandling:
    """Class for error handling."""

    def __init__(self):
        pass

    def string_error_handler(self, user_input, length, white_space_is_valid = False):
        """Function for string error handling."""
        if white_space_is_valid and len(str(user_input).strip()) == 0:
            user_input = '.'

        error_occured = False

        if len(str(user_input).strip()) == 0:
            error.whitespace()
            error_occured = True
        elif user_input.isnumeric():
            error.type('str')
            error_occured = True
        elif len(user_input) >= 100:
            error.length(length)
            error_occured = True
        else:
            error_occured = False

        return error_occured

    def int_error_hander(self, user_input, lower_bound, upper_bound, white_space_is_valid = False):
        """Function for integer error handling."""
        if white_space_is_valid and len(user_input) == 0:
            user_input = '.'

        error_occured = False

        if len(str(user_input)) == 0:
            error.whitespace()
            error_occured = True
        elif user_input.isalpha():
            error.type('int')
            error_occured = True
        elif lower_bound > user_input > upper_bound:
            error.range(lower_bound, upper_bound)
            error_occured = True
        else:
            error_occured = False

        return error_occured

