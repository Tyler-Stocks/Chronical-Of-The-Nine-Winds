"""
Class for error handling.
Structure:
ErrorHandling
|
|--__init__(self) -> None
|
|--string_error_handler(self, user_input(str), length(int | float), white_space_is_valid(bool) = False) -> bool
|
|--int_error_handler(self, user_input(int), lower_bound(int | float), upper_bound(int | float), white_space_is_valid(bool) = False) -> bool
"""
from utility import custom_errors

error = custom_errors.InputErrors()

class ErrorHandling:
    """Class for error handling."""

    def __init__(self) -> None:
        pass

    def string_error_handler(self, user_input: str, length: int | float, white_space_is_valid: bool = False) -> bool:
        """
        Function for string error handling.

        Args:
            user_input (str): The input to be evaluated.
            length (int): The maximum allowed input length.
            white_space_is_valid (bool), default False: If set to True no input becomes valid.

        Returns:
            error_occured (bool): Returns True or False depending on whether an error was detected.
        """
        white_space_test = 0

        if white_space_is_valid and len(str(user_input).strip()) == 0:
            white_space_test = 1

        error_occured = False

        if len(str(user_input).strip()) == white_space_test:
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

    def int_error_hander(self, user_input: str, lower_bound: int | float, upper_bound: int | float, white_space_is_valid: bool = False) -> bool:
        """
        Function for integer error handling.

        Args:
            user_input (int): The input to be evaluated.
            lower_bound (int): The lowest valid value
            upper_bound (int): The highest valid value
            white_space_is_valid (bool), default False: If True allowes no input as a valid input.
        """
        if white_space_is_valid and len(user_input) == 0:
            user_input = '.'

        error_occured = False

        if len(str(user_input)) == 0:
            error.whitespace()
            error_occured = True
        elif user_input.isalpha():
            error.type('int')
            error_occured = True
        elif lower_bound > int(user_input) > upper_bound:
            error.range(lower_bound, upper_bound)
            error_occured = True
        else:
            error_occured = False

        return error_occured

