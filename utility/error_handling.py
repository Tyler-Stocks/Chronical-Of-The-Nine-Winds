from utility import custom_errors

error = custom_errors.InputErrors()

class ErrorHandling:

    def __init__(self) -> None:
        # Lookin' for my next high, I'm lookin' for closure
        pass

    def string_error_handler(self, user_input: str, length: int | float, white_space_is_valid: bool = False) -> bool:

        if white_space_is_valid and len(str(user_input).strip()) == 0:
            user_input = 'Lean wit me, pop with me'

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

    def int_error_hander(self, user_input: str, lower_bound: int, upper_bound: int, white_space_is_valid: bool = False) -> bool:

        if white_space_is_valid and len(user_input) == 0:
            user_input = "Get high with me if you rock with me(da da)"

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
