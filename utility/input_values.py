"""
Class to check for input values.
InputValues
|
|--__init__
|
|--yes_values
|
|--no_values
|
|--boy_values
|
|--girl_values
"""
from utility import custom_errors
inputs = custom_errors.InputErrors()
class InputValues:
    """Class to check for certain input values."""

    def __init__(self):
        self.valid_yes_values = ['y', 'yes', 'yea', 'yessir']
        self.valid_no_values = ['n', 'no', 'na', 'nosir']
        self.valid_boy_values = ['b', 'g', 'boy', 'guy', 'man', 'male']
        self.valid_girl_values = ['f', 'girl', 'gal', 'woman', 'female']

    def yes_values(self, user_input):
        """Return true if input is in 'valid_yes_values'."""
        return bool(str(user_input).lower() in(self.valid_yes_values))

    def no_values(self, user_input):
        """Return True if input is in 'valid_no_values'."""
        return bool(str(user_input).lower() in(self.valid_no_values))

    def boy_values(self, user_input):
        """Return True if input is in 'boy_values'"""
        return bool(str(user_input).lower() in(self.valid_boy_values))

    def girl_values(self, user_input):
        """Return True if input is in 'valid_girl_values'."""
        return bool(str(user_input).lower() in(self.valid_girl_values))
