from utility import custom_errors
inputs = custom_errors.InputErrors()

class InputValues:

    valid_yes_values = ['y', 'yes', 'yea', 'yessir']
    valid_no_values = ['n', 'no', 'na', 'nosir']
    valid_boy_values = ['b', 'g', 'boy', 'guy', 'man', 'male']
    valid_girl_values = ['f', 'girl', 'gal', 'woman', 'female']

    def __init__(self) -> None:
        pass

    def yes_values(self, user_input: str) -> bool:
        return bool(str(user_input).lower() in(self.valid_yes_values))

    def no_values(self, user_input: str) -> bool:
        return bool(str(user_input).lower() in(self.valid_no_values))

    def boy_values(self, user_input: str) -> bool:
        return bool(str(user_input).lower() in(self.valid_boy_values))

    def girl_values(self, user_input: str) -> bool:
        return bool(str(user_input).lower() in(self.valid_girl_values))
