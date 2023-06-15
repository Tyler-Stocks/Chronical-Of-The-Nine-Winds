import math

class InputUtility:

    def __init__(self):
        # Smoke wit me, drink wit me
        pass

    def integer(self, user_input: int | float, data_type: float) -> int | float:
        if data_type == 'int':
            return int(user_input)
        elif data_type == 'float':
            return float(user_input)
        else:
            pass

        return user_input

    def string(self, user_input: str) -> str:
            return str(user_input).strip().capitalize()
