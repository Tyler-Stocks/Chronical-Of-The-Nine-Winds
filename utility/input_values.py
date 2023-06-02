"""
Class to check for input values.
InputValues
|
|--__init__(self, user_input(str)) -> bool
|
|--yes_values(self, user_input(str)) -> bool
|
|--no_values(self, user_input(str)) -> bool
|
|--boy_values(self, user_input(str)) -> bool
|
|--girl_values(self, user_input(str)) -> bool
"""
from utility import custom_errors
inputs = custom_errors.InputErrors()
class InputValues:
    """Class to check for certain input values."""

    valid_yes_values = ['y', 'yes', 'yea', 'yessir']
    valid_no_values = ['n', 'no', 'na', 'nosir']
    valid_boy_values = ['b', 'g', 'boy', 'guy', 'man', 'male']
    valid_girl_values = ['f', 'girl', 'gal', 'woman', 'female']

    def __init__(self) -> None:
        pass

    def yes_values(
            self,
            user_input: str
            ) -> bool:
        """Return true if input is in 'valid_yes_values'."""
        return bool(str(user_input).lower() in(self.valid_yes_values))

    def no_values(
            self,
            user_input: str
            ) -> bool:
        """Return True if input is in 'valid_no_values'."""
        return bool(str(user_input).lower() in(self.valid_no_values))

    def boy_values(
            self,
            user_input: str
            ) -> bool:
        """Return True if input is in 'boy_values'"""
        return bool(str(user_input).lower() in(self.valid_boy_values))

    def girl_values(
            self,
            user_input: str
            ) -> bool:
        """Return True if input is in 'valid_girl_values'."""
        return bool(str(user_input).lower() in(self.valid_girl_values))
