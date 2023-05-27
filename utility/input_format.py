"""
Class for different utility surrounding input utility
Structure:
    StringUtility
    |
    |--__init__
    |
    |--format_string
"""
import math
class InputUtility:
    """Class for Import Utility"""

    def __init__(self):
        pass

    def string(self, user_input):
        """Takes in user input, then formats it."""

        user_input = str(user_input).capitalize().strip()

        return user_input

    def integer(self, user_input, round_type):
        """Return rounded user input rounded, and in desired data type"""

        if round_type == 'Ten':
            return math.ceil(user_input / 10) * 10
        elif round_type == 'Hundred':
            return math.ceil(user_input / 100) * 100
        elif round_type == 'Thousand':
            return math.ceil(user_input / 1000) * 1000
        else:
            math.ceil(user_input)
