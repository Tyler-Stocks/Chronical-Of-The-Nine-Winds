"""
Class for different utility surrounding strings.
Structure:
    StringUtility
    |
    |--__init__
    |
    |--format_string
"""
class StringUtility:
    """Class for string utility"""

    def __init__(self):
        pass

    def format_string(self, user_input):
        """Takes in user input, then formats it."""

        user_input = str(user_input).capitalize().strip()

        return user_input
