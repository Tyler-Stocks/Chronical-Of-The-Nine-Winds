"""
Class for different utility surrounding input utility
Structure:
    InputUtility
    |
    |--__init__(self) -> None
    |
    |--string(self, user_input(str)) -> str
    |
    |--integer(self, user_input(int)) -> int | float
"""
import math
class InputUtility:
    """Class for Input Utility"""

    def __init__(self):
        pass

    def string(
            self,
            user_input: str
            ) -> str:
        """
        Takes in user input, then returns a formatted version.

        Args:
            user_input (str): Input to be formatted

        Return:
            user_input (str): A capitalized stripped version of the 'user_input' variable
        """

        user_input = str(user_input).capitalize().strip()

        return user_input

    def integer(
            self,
            user_input: int | float,
            round_type: str,
            data_type: str
            ) -> int | float:
        """
        Takes in integer input, then formats it.

        Args:
            user_input (int): Input to be formatted
            round_precision (str): Percision to round to
            data_type (str): Data type to be converted to

        Return:
            user_input (int, float): A rounded, converted version of the 'user_input' variable
        """

        if round_type == 'Ten':
            return math.ceil(user_input / 10) * 10
        elif round_type == 'Hundred':
            return math.ceil(user_input / 100) * 100
        elif round_type == 'Thousand':
            return math.ceil(user_input / 1000) * 1000

        if data_type == 'int':
            user_input = int(user_input)
        elif data_type == 'float':
            user_input = float(user_input)
        else:
            raise TypeError

        return user_input