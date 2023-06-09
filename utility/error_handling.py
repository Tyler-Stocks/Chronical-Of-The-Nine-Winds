from utility import custom_errors

error = custom_errors.InputErrors()

class ErrorHandling:

    def __init__(self) -> None:
        pass

    def string_error_handler(
        self,
        user_input: str,
        length: int | float,
        white_space_is_valid: bool = False
        ) -> bool:

        if white_space_is_valid and len(str(user_input).strip()) == 0:
            user_input = 'I admit it, another hoe got me finished'

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

    def int_error_hander(
            self,
            user_input: str,
            lower_bound: int | float,
            upper_bound: int | float,
            white_space_is_valid: bool = False
        ) -> bool:

        if white_space_is_valid and len(user_input) == 0:
            user_input = "Broke my heart, oh, no you didn't."

        error_occured = False

        if len(str(user_input.strip)) == 0:
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
