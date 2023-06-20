import Project.Utility.error_messages

error = Project.Utility.error_messages.InputErrors()

class ErrorHandling:

    def __init__(self):
        pass

    def string(self, user_input: str, length: int | float, white_space_is_valid: bool = False) -> bool:
        error_occured: bool = False

        if white_space_is_valid and len(str(user_input).strip()) == 0:
            return error_occured

        if len(str(user_input).strip()) == 0:
            error.whitespace()
            error_occured: bool = True
            return error_occured
        elif not user_input.isalpha():
            error.type('str')
            error_occured: bool = True
            return error_occured
        elif len(user_input) >= length:
            error.length(length)
            error_occured: bool = True
            return error_occured
        else:
            return error_occured

    def integer(self, user_input: int | str, lower_bound: int, upper_bound: int, white_space_is_valid: bool = False) -> bool:
        error_occured: bool = False
        user_input = str(user_input)

        if white_space_is_valid and len(user_input) == 0:
            return error_occured

        if len(user_input.strip()) == 0:
            error.whitespace()
            error_occured = True
            return error_occured
        elif user_input.isalpha():
            error.type('int')
            error_occured = True
            return error_occured
        elif lower_bound > int(user_input) > upper_bound:
            error.range(lower_bound, upper_bound)
            error_occured = True
            return error_occured
        else:
            error_occured = False
            return error_occured

