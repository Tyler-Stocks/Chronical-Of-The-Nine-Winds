from Project.Utility import error_messages

error = error_messages.InputErrors()

class ErrorHandling:

    def __init__(self):
        pass

    def string(self, user_input, length, white_space_is_valid = False) -> bool:
        error_occured = False

        if white_space_is_valid and len(str(user_input).strip()) == 0:
            pass
        if len(str(user_input).strip()) == 0:
            error.whitespace()
            error_occured = True
        elif not user_input.isalpha():
            error.type('Input must be alphabetical')
            error_occured = True
        elif len(user_input) >= length:
            error.length(length)
            error_occured = True
        return error_occured

    def integer(self, user_input, lower_bound, upper_bound, white_space_is_valid = False) -> bool:
        error_occured = False

        if white_space_is_valid and len(str(user_input).strip()) == 0:
            pass
        if len(str(user_input).strip()) == 0:
            error.whitespace()
            error_occured = True
        elif str(user_input).isalpha():
            error.type('Input must be an integer.')
            error_occured = True
        elif lower_bound > int(user_input) > upper_bound:
            error.range(lower_bound, upper_bound)
            error_occured = True
        return error_occured

